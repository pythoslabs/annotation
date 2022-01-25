# Convert an annotation matlab  file (.mat )  to .json file 
# For Caltech 101 dataset ( whose annotations are in .mat files )

import scipy.io.matlab as mio
from scipy import array
import re, pprint
import sys
import os 


def mat_to_json(matfile,jsonfile):

    mat = mio.loadmat(matfile)
    fd=open(jsonfile,'w')
    
    for k,v in mat.items():
        if k.startswith("__"):
            continue
        try:
            if 1 in v.shape:
                v=v.flatten()
            l = v.tolist()
            fd.write(k+" = ")
            pprint.pprint(l, fd, indent=4)
        except Exception as e1:
            print (f"Error processing {k} : {e1}")
    fd.close()

def change_extension(fname) :
    f_new = fname.replace('.mat','.json')
    return f_new

DIR_MAT = '../data/airplane_mat'
DIR_OUTPUT =  '../data/airplane_json'

for fname in os.listdir(DIR_MAT):
    f_new =change_extension(fname)
    mat_to_json(f'{DIR_MAT}/{fname}', f'{DIR_OUTPUT}/{f_new}')


    
