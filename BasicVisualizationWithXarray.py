import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

ds = xr.tutorial.open_dataset("air_temperature_gradient")
print(ds)
# Tair is a three dimensional variable, made up of the horizontal gradients: dTdx and dTdy as well as time.
# ds.isel(lat=10, lon=10)
# plt.hist(ds.Tair.plot())
# ds.Tair.plot()
# plt.savefig('test1.png')

