#!/usr/bin/env python3
#
# nc2npy_j3
#
# sample_03.py
#----------------------------------------------------------------------- 
import netCDF4
import numpy as np
from j3 import misc

# directory path to downloaded netCDF
data_path='../../J3_DAILY'

# 
var='NHF'
ver='V1.0'
tr='DAILY'
sr='HR'
yr='2002'

fname = misc.filename(var,tr,sr,ver,yr)
file=data_path + '/' + fname
print(file)

# open netCDF file
ncf = netCDF4.Dataset(file, 'r')

# define variable
nhf = ncf.variables[var][:]

# output
ofile = 'J-OFURO3_'+var + '_' + tr + '_' + sr + '_' + yr
nhf_filled = np.ma.filled(nhf,nhf.fill_value)
np.save(ofile,nhf_filled)
