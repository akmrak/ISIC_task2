import numpy as np
import h5py
import pickle
import itertools
from PIL import Image

def area_size(names,i):
	image_1=names[i]
	image_1_1=Image.open(image_1)	
	width,height = image_1_1.size
	image_1_list=list(image_1_1.getdata())
	count=0	
	for k in range(len(image_1_list)):
		if(image_1_list[k]==255):
			count+=1
	#count_normal=(count*1.0)/len(sum_image_list)
	return (count,width,height)

def area_driver(names):
	count_combinations=5
	matrix_area=np.zeros((len(names),count_combinations))
	matrix_total_area=np.zeros((len(names),2))
	
	for count_name,name in enumerate(names):
		print (count_name)
		list_combinations=itertools.combinations([1,2,3,4,5],1)
		for count,combs in enumerate(list_combinations):
			value=area_size(name,combs[0])
			matrix_area[count_name][count]=value[0]
			if(count==0):
				matrix_total_area[count_name][0]=value[1]
				matrix_total_area[count_name][1]=value[2]
			print ("**count vs name**")	
			print (count,combs[0])
			print ("**end within image iteration**")
		print ("**end iteration**")
	return (matrix_area,matrix_total_area)
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
	(matrix_area,matrix_total_area)=area_driver(list_names)	
	print (list_names)
	print (matrix_area)
	print (matrix_total_area)
	#print (matrix_overlap)
	h5f = h5py.File('/users/PAS0272/osu10258/data/data_attribute_area.h5', 'w')
	h5f.create_dataset('area_matrix', data=matrix_area)
	h5f.close()
	h5f1=h5py.File('/users/PAS0272/osu10258/data/data_total_area.h5','w')
	h5f1.create_dataset('area_matrix_total',data=matrix_total_area)
	h5f1.close()

if __name__ == "__main__":
	main()
