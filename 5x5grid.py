import numpy as np
import h5py
import pickle
import itertools
from PIL import Image

def overlap_size(names,i,j):
	image_1=names[i]
	image_2=names[j]
	image_1_1=Image.open(image_1)	
	image_2_2=Image.open(image_2)
	image_1_list=list(image_1_1.getdata())
	image_2_list=list(image_2_2.getdata())
	sum_image_list=[sum(x) for x in zip(image_1_list,image_2_list)]
	count=0	
	for k in range(len(sum_image_list)):
		if(sum_image_list[k]>255):
			count+=1
	count_normal=(count*1.0)/len(sum_image_list)
	return count_normal

def overlap_driver(names):
	count_combinations=10
	matrix_overlap=np.zeros((len(names),count_combinations))
	
	for count_name,name in enumerate(names):
		print (count_name)
		list_combinations=itertools.combinations([1,2,3,4,5],2)
		for count,combs in enumerate(list_combinations):
			value=overlap_size(name,combs[0],combs[1])
			matrix_overlap[count_name][count]=value	
			print ("**count vs name**")	
			print (count)
			print (name[combs[0]],name[combs[1]])
			print ("**end within image iteration**")
		print ("**end iteration**")
	return matrix_overlap
def main():
	list_names=pickle.load(open("/users/PAS0272/osu10258/data/a3.pickle","rb"))
	#print (len(list_names))
	#overlap_driver(list_names[0])
	#print (a)
	#name=list_names[449]
	#name_1=name[1]
	#name_2=name[2]
	#print (name_1,name_2)
	#a=[1,2,3]
	#a_np=np.asarray(a)
	#list_names=list_names[449]
	#list_names=[list_names]
	matrix_overlap=overlap_driver(list_names)	
	#print (matrix_overlap)
	h5f = h5py.File('/users/PAS0272/osu10258/data/data.h5', 'w')
	h5f.create_dataset('overlap_matrix', data=matrix_overlap)
	h5f.close()



if __name__ == "__main__":
	main()
