#!/usr/bin/env python3
#
# j3.misc.py
#--------------------------------------------------  
def get_argv():
    import sys
    nargv = len(sys.argv)
    if nargv == 3:
      var = sys.argv[1]
      yr1 = sys.argv[2]
      yr2 = yr1
    elif nargv == 4:
      var = sys.argv[1]
      yr1 = sys.argv[2]
      yr2 = sys.argv[3]
    elif nargv == 1:
      var_list()
      eos()
    else:
      error(1)
      usage()
      eos()
    return(var,yr1,yr2)

def header(version):
    print ('---------------------------')
    print (' read_j3.py'+'  '+version)
    print ('---------------------------')

def setup():
    tr='DAILY'
    sr='HR'
    ver='V1.0'
    return(tr,sr,ver)

def var_name():
    var_names = ['LHF', 'SHF', 'SWR', 'LWR', 'NHF',\
            'ULWR', 'DLWR', 'TAUX', 'TAUY', 'FWF', 'EVAP', 'RAIN',\
            'SST', 'WND', 'UWND', 'VWND', 'QA', 'QS', 'DQ', 'TA10','DT']
    return(var_names)

def filename(var,tr,sr,ver,year):
     fname = 'J-OFURO3_' + var + '_' + ver + '_' + tr + '_' + sr + '_' + year + '.nc'
     return(fname)
