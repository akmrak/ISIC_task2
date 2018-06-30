import statistics
import itertools
import h5py
import numpy as np 
np.set_printoptions(threshold=np.inf)
h5f = h5py.File('/users/PAS0272/osu10258/data/data.h5','r')
intersection_matrix = h5f['overlap_matrix'][:]
h5f.close()
h5f = h5py.File('/users/PAS0272/osu10258/data/data_attribute_area.h5','r')
attribute_area_matrix = h5f['area_matrix'][:]
h5f.close()
h5f = h5py.File('/users/PAS0272/osu10258/data/data_total_area.h5','r')
size_matrix = h5f['area_matrix_total'][:]
h5f.close()
print([a for a in attribute_area_matrix[:,0] if a!=0])
temp=[[],[],[],[],[]]
for i in range(5):
	for count,a in enumerate(attribute_area_matrix[:,i]):
		if(a!=0):	
			temp[i].append(a/(size_matrix[count][0]*size_matrix[count][1]))
for i in range(5):
	print(statistics.mean(temp[i]))	
		
		
