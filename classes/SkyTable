class SkyTable:

  def __init__(self, dataframe, dec="DEC", ra="RA"):
    self.dataframe = dataframe.copy()
    self.dataframe = self.dataframe.rename(columns = {dec:"DEC",ra:"RA"})
    #print(dec,ra)
    #print(self.dataframe)
    self.statistics()

  def statistics(self):
    min_ra = np.min(np.array(self.dataframe["RA"]))
    min_dec = np.min(np.array(self.dataframe["DEC"]))
    self.min = {"RA": min_ra, "DEC": min_dec}
    max_ra = np.max(np.array(self.dataframe["RA"]))
    max_dec = np.max(np.array(self.dataframe["DEC"]))
    self.max = {"RA": max_ra, "DEC": max_dec}
    mean_ra = np.mean(np.array(self.dataframe["RA"]))
    mean_dec = np.mean(np.array(self.dataframe["DEC"]))
    self.mean = {"RA": mean_ra, "DEC": mean_dec}

  def transform(self, move = [0,0], resize = 1):
    new_df = self.dataframe.copy()
    new_df["RA"] = new_df["RA"]+move[1]
    new_df["DEC"] = new_df["DEC"]+move[0]
    mean_ra = np.mean(np.array(new_df["RA"]))
    mean_dec = np.mean(np.array(new_df["DEC"]))
    new_df["RA"] = mean_ra + (new_df["RA"] - mean_ra)*resize
    new_df["DEC"] = mean_dec + (new_df["DEC"] - mean_dec)*resize
    return SkyTable(new_df)

  def add_noise(self, distribution_type="normal",param=[0,1]):
    if distribution_type=="normal":
      fun = np.random.normal
    if distribution_type=="uniform":
      fun = np.random.uniform
    noise_dec = fun(*param,len(self.dataframe))
    noise_ra = fun(*param,len(self.dataframe))
    new_df = self.dataframe.copy()
    new_df["RA"] = new_df["RA"]+noise_ra
    new_df["DEC"] = new_df["DEC"]+noise_dec
    return SkyTable(new_df)

  def cut(self,cut_dec=[0,1],cut_ra=[0,1]):
    new_df = self.dataframe[(self.dataframe["RA"]>cut_ra[0])&
                            (self.dataframe["RA"]<cut_ra[1])&
                            (self.dataframe["DEC"]>cut_dec[0])&
                            (self.dataframe["DEC"]<cut_dec[1])]
    return SkyTable(new_df)
  
  def cut_centrize(self,cut_dec=1,cut_ra=1):
    return self.cut([self.mean["DEC"]-cut_dec,self.mean["DEC"]+cut_dec],
                    [self.mean["RA"]-cut_ra,self.mean["RA"]+cut_ra])


  def get_dec(self):
    return np.array(self.dataframe["DEC"])
  def get_ra(self):
    return np.array(self.dataframe["RA"])
  def min(self):
    return self.min
  def max(self):
    return self.max
  def get_df(self):
    return self.dataframe

  def draw_density_np(self,bins = [20,20]):
    plt.hist2d(self.get_dec(),self.get_ra(),bins = bins)
  

  
sky = SkyTable(df_opt,"OPT_DEC","OPT_RA")
sky.transform(move = [10,10],resize = 10).add_noise("uniform",param=[-20,20]).cut_centrize(10,10).draw_density_np([50,50])
