import pickle
import h5py
import numpy  as np
import itertools
import statistics
from PIL import Image

string_names="/users/PAS0272/osu10258/data/a3.pickle"
attribute_count=5
base_string="/users/PAS0272/osu10258/data/augmented_data/"
count_base_no=0
base_image_ht=224
base_image_wd=224
stride_length=45
count_1=[0,0,0,0,0]
count_0=[0,0,0,0,0]
def check_matrix(image,mask):
	median_image=np.median(mask)
	#print(mask.shape)
	#median_image=1
	#print(image.shape,mask.shape)
	#print(mask)
	if(median_image==255):
		return(1)
	else:
		return(0)
def generate_augmented_images(names,attribute):
	original_image_url=names[0]
	image_mask_url=names[attribute]
	#print(original_image_url,image_mask_url)
	original_image=Image.open(original_image_url)
	wd,ht=original_image.size
	image_mask=Image.open(image_mask_url)
	original_image=np.array(original_image)
	image_mask=np.array(image_mask)
	i=0
	j=0
	#print(wd,ht)
	#print(original_image.shape,image_mask.shape)
	val_1=0
	val_0=0
	while(j+base_image_ht<ht):
		i=0
		while(i+base_image_wd<wd):
			#print(i,i+base_image_wd,j,j+base_image_ht)
			#print(original_image[i:i+base_image_wd,j:j+base_image_ht,:].shape,image_mask[i:i+base_image_wd,j:j+base_image_ht].shape)
			#print(i,i+base_image_wd,j,j+base_image_ht)
			i1=i+base_image_wd
			j1=j+base_image_ht
			check=check_matrix(original_image[j:j1,i:i1,:],image_mask[j:j1,i:i1])
			#print(i,i1,j,j1)
			#print(original_image[j:j1,i:i1,:].shape,image_mask[j:j1,i:i1].shape)
			#print(check)	
			if(check==1):
				val_1+=1
			else:
				val_0+=1
			i+=stride_length
		j+=stride_length
	#print(val_0,val_1)	
	count_0[attribute-1]+=val_0
	count_1[attribute-1]+=val_1
def generate_driver(names):
	#attribute_count=1
	for attribute_num in range(attribute_count):
		for name in names:
			generate_augmented_images(name,attribute_num+1)
def main():
	list_names=pickle.load(open(string_names,"rb"))
	#list_names=list_names[:2]
	generate_driver(list_names)	
	print(count_0,count_1)
if __name__ == "__main__":
	main()

