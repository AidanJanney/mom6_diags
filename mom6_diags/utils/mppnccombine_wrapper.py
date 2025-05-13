import subprocess
import argparse
import sys
import os
import glob

######### WARNING WARNING ###########
# Writing this script before other functionality of mom6_diags
# is in place, so it will need to be updated
# should still be a useful skeleton for the future script
# this will also be mostly deprecated in the future after 
# CESM3_0_beta06 with auto_merge_nc in input.nml for MOM6 
######### WARNING WARNING ###########

def options():
    parser = argparse.ArgumentParser(description=
        '''
        Script for merging distributed netCDF files from FMS (parallel I/O manager 
        for MOM6). This is most useful for large numbers of distributed files produced 
        for many different passages/transects over a long period of time.
        '''
        )
    parser.add_argument('-i','--inputdir', type=str, default='',help='''Directory containing distributed netCDF files.''')
    
    
def mppnccombine_auto(casename, passages = None):
    