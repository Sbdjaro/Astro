import astropy as a
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
import astropy.units as u
from collections import Counter
from matplotlib.pyplot import figure


def add_range_to_dataframe(df, first_name=['ra','de'], second_name=['raMean','decMean']):
  """
  Add range between two objects in Dataframe
  """
  c1 = SkyCoord(ra = np.array(df[first_name[0]])*u.degree,dec = np.array(df[first_name[1]])*u.degree)
  c2 = SkyCoord(ra = np.array(df[second_name[0]])*u.degree,dec = np.array(df[second_name[1]])*u.degree)
  sep = c1.separation(c2)
  new_df = df.copy()
  new_df["distance"] = sep.arcsecond
  return new_df
  
def read_csv(filename,col_id_1,col_id_2,col_cord_1=["ra","de"],col_cord_2=["raMean","decMean"]):
  """
  Read csv correlated table between two collections with collum col_id_1 - first ID, col_id_2 - second ID,
  col_cord_1 - name of [RA,DEC] first object,col_cord_2 - name of [RA,DEC] second object
  """
  df = pd.read_csv(filename)
  df = df.rename(columns={col_id_1:"Chandra_ID"})
  df = df.rename(columns={col_id_2:"Optic_ID"})
  df = df.rename(columns={col_cord_1[0]:"Chandra_RA"})
  df = df.rename(columns={col_cord_1[1]:"Chandra_DEC"})
  df = df.rename(columns={col_cord_2[0]:"Optic_RA"})
  df = df.rename(columns={col_cord_2[1]:"Optic_DEC"})
  df = df[((df["Chandra_RA"]-df['Optic_RA'])**2 + (df["Chandra_DEC"]-df['Optic_DEC'])**2)**0.5<0.1]
  df = add_range_to_dataframe(df)
  return df
 
  
def calc_radius(density,probability):
  """
  Calculate the radius with which the error is small
  """
  return (-np.log(1-probability)/density/np.pi)**0.5
  
def select_true(df,rad):
  return df[df["distance"]<rad]
  
def delete_obj_in_list(df,l):
  return df.query(f'Chandra_ID in @l')
  
def get_frequency(df,t):
  """
  Finde object whith quantity of near association lower then t 
  """
  c = Counter(df["Chandra_ID"])
  count = c.most_common(len(df["Chandra_ID"].unique()))
  count_df = pd.DataFrame(count)
  return count_df[count_df[1]<t]
  
def delete_mult_obj(df,name = "Chandra_ID"):
  """
  Clear lines with objects repeated several times
  """
  new_df=df[name]
  a = Counter(list(new_df))
  b = Counter(new_df.unique())
  bad = list(a-b)
  return df.query(f'{name} not in @bad')
  
def clear_df(df,mult):
  area = np.pi*30*30
  density = df["Chandra_ID"].unique().__len__()/(area)
  density = mult/area
  g_df = select_true(df,calc_radius(density,0.05))
  freq = get_frequency(df,mult)
  good_df = delete_obj_in_list(g_df,np.array(freq[0]))
  good_df = delete_mult_obj(good_df)
  good_df = delete_mult_obj(good_df,"Optic_ID")
  return good_df

def make_good_df(filename,col_id_1,col_id_2,col_cord_1=["ra","de"],col_cord_2=["raMean","decMean"]):
  """
  Prepare table csv correlated table between two collections with collum col_id_1 - first ID, col_id_2 - second ID,
  col_cord_1 - name of [RA,DEC] first object,col_cord_2 - name of [RA,DEC] second object
  """
  df = read_csv(filename,col_id_1,col_id_2,col_cord_1=col_cord_1,col_cord_2=col_cord_2)
  return clear_df(df,60)
  
def plot_size_depend_on_num(df):
  l=[]
  for mult in range(10,100,2):
    f = make_good_df(df,mult)
    l.append(len(f))
  l = np.array(l)
  plt.plot(l[:,0],l[:,1])
  return l
