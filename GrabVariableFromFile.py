import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

filename =  '/home/users/dwest77/tbworkexp/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20071001052359z_20071001070551z_750_799-v1000.nc'
group1 = xr.open_dataset(filename)
print(group1.variables)