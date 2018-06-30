import itertools
import h5py
import numpy as np 
import statistics
np.set_printoptions(threshold=np.inf)
def load_matrices():
	h5f = h5py.File('/users/PAS0272/osu10258/data/data.h5','r')
	intersection_matrix = h5f['overlap_matrix'][:]
	h5f.close()
	h5f = h5py.File('/users/PAS0272/osu10258/data/data_attribute_area.h5','r')
	attribute_area_matrix = h5f['area_matrix'][:]
	h5f.close()
	h5f = h5py.File('/users/PAS0272/osu10258/data/data_total_area.h5','r')
	size_matrix = h5f['area_matrix_total'][:]
	h5f.close()
	return (intersection_matrix,attribute_area_matrix,size_matrix)	
def dice_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix):
	dice_matrix=np.zeros(intersection_matrix.shape)	
	height,width=intersection_matrix.shape	
	for i in range(height):
		list_combinations=itertools.combinations([1,2,3,4,5],2)
		for j,combs in enumerate(list_combinations):
			intersection_area=intersection_matrix[i][j]*size_matrix[i][0]*size_matrix[i][1]
			union_area=attribute_area_matrix[i][combs[0]-1]+attribute_area_matrix[i][combs[1]-1]-intersection_area
			if(attribute_area_matrix[i][combs[0]-1]!=0 and attribute_area_matrix[i][combs[1]-1]!=0):	
				dice_matrix[i][j]=2*intersection_area/(attribute_area_matrix[i][combs[0]-1]+attribute_area_matrix[i][combs[1]-1])
			else:
				dice_matrix[i][j]=-1
	return dice_matrix

def first_attribute_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix):
	a1_matrix=np.zeros(intersection_matrix.shape)	
	height,width=intersection_matrix.shape	
	for i in range(height):
		list_combinations=itertools.combinations([1,2,3,4,5],2)
		for j,combs in enumerate(list_combinations):
			intersection_area=intersection_matrix[i][j]*size_matrix[i][0]*size_matrix[i][1]
			area=attribute_area_matrix[i][combs[0]-1]
			if(attribute_area_matrix[i][combs[0]-1]!=0 and attribute_area_matrix[i][combs[1]-1]!=0):	
				a1_matrix[i][j]=intersection_area/area	
			else:
				a1_matrix[i][j]=-1
	return a1_matrix


def second_attribute_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix):
	a2_matrix=np.zeros(intersection_matrix.shape)	
	height,width=intersection_matrix.shape	
	for i in range(height):
		list_combinations=itertools.combinations([1,2,3,4,5],2)
		for j,combs in enumerate(list_combinations):
			intersection_area=intersection_matrix[i][j]*size_matrix[i][0]*size_matrix[i][1]
			area=attribute_area_matrix[i][combs[1]-1]
			if(attribute_area_matrix[i][combs[0]-1]!=0 and attribute_area_matrix[i][combs[1]-1]!=0):
				a2_matrix[i][j]=intersection_area/area	
			else:
				a2_matrix[i][j]=-1
	return a2_matrix


def main():
	intersection_matrix,attribute_area_matrix,size_matrix=load_matrices()
	dice_matrix=second_attribute_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix)
	temp=[[],[],[],[],[],[],[],[],[],[]]
	for i in range(10):
		dice=[a[i] for a in dice_matrix if a[i]!=-1]
		print(statistics.mean(dice))
	#a1_matrix=first_attribute_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix)
	#print (a1_matrix)	
	#a2_matrix=second_attribute_matrix_create(intersection_matrix,attribute_area_matrix,size_matrix)
	#print (a2_matrix)	
if __name__ == "__main__":
	main()
