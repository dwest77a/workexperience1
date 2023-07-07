import numpy as np
import xarray as xr

np.random.seed(0)

#Dataset takes three parameters: data_vars, coords, attrs. 
ds1 = xr.Dataset(
    data_vars={
        "a": (("x", "y"), np.random.randn(4, 2)),
        "b": (("z", "x"), np.random.randn(6, 4)),
    },
    coords={
        "x": np.arange(4),
        "y": np.arange(-2, 0),
        "z": np.arange(-3, 3),
    },
)

ds2 = xr.Dataset(
    data_vars={
        "a": (("x", "y"), np.random.randn(7, 3)),
        "b": (("z", "x"), np.random.randn(2, 7)),
    },
    coords={
        "x": np.arange(6, 13),
        "y": np.arange(3),
        "z": np.arange(3, 5),
    },
)

#now that they are created, to write to thew data sets:
ds1.to_netcdf("ds1.nc")
ds2.to_netcdf("ds2.nc")

# write to data array now
ds1.a.to_netcdf("da1.nc")



#to read:
#print(xr.open_dataset("ds1.nc"))
# or:
#print(xr.open_dataarray("da1.nc").a)
filename =  '/work/scratch-nopw/tbworkexp/ral-l2p-tqoe-iasi_mhs_amsu_metopa-tir_mw-20070710172654z_20070710190558z_700_749-v1000.nc'
#print(dir(xr.open_mfdataset(filename)))
print(xr.open_mfdataset(filename).latitude)
# dataset = xr.tutorial.open_dataset(filename)
# print(dataset.latitude)