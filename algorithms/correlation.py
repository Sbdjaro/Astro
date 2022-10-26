import astropy as a
import numpy as np
import pandas as pd


from astropy.table import Table
dat = Table.read('example1.fits', format='fits')
df = dat.to_pandas()

dat = Table.read('COSMOS_IRAC.fits', format='fits')
df_irac = dat.to_pandas()
df_irac = df_irac.rename(columns={'RA': 'IRAC_RA', 'DEC': 'IRAC_DEC'})

dat = Table.read('COSMOS_OPTICAL.fits', format='fits')
df_opt = dat.to_pandas()
df_opt = df_opt.rename(columns={'RA': 'OPT_RA', 'DEC': 'OPT_DEC','ID':'OPT_ID'})

import astropy.units as u
from astropy.coordinates import SkyCoord 

c = SkyCoord(ra = df_opt["OPT_RA"]*u.degree,dec = df_opt["OPT_DEC"]*u.degree)
catalog = SkyCoord(ra = df_irac["IRAC_RA"]*u.degree,dec = df_irac["IRAC_DEC"]*u.degree)
idx,d2d,d3d = c.match_to_catalog_sky(catalog)
idx1,idxcatalog,d2d1,d3d1 = catalog.search_around_sky(c,0.001*u.deg)
