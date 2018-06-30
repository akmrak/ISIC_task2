import h5py
import numpy as np 
import pickle
import statistics
import itertools
h5f = h5py.File('/users/PAS0272/osu10258/data/data.h5','r')
b = h5f['overlap_matrix'][:]
h5f.close()
list2=pickle.load(open("/users/PAS0272/osu10258/data/a2.pickle","rb"))
a=[]
a_length=[]
list_combinations=itertools.combinations([1,2,3,4,5],2)
for count,combs in enumerate(list_combinations):
	mean_individual=[]
	for i in range(b.shape[0]):
		comb_1=combs[0]
		comb_2=combs[1]
		if(list2[i][comb_1]==1 and list2[i][comb_2]==1):
			print (comb_1,comb_2,list2[i])
			mean_individual.append(b[i][count])
	a.append(statistics.mean(mean_individual))
	a_length.append(len(mean_individual))
print (a)
print (a_length)
print (np.mean(b,axis=0))
list_combinations=itertools.combinations([1,2,3,4,5],2)	
for it in list_combinations:
	print (it)
