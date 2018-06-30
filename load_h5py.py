import h5py
import numpy as np 
h5f = h5py.File('/users/PAS0272/osu10258/data/data.h5','r')
b = h5f['overlap_matrix'][:]
h5f.close()
print (b)

