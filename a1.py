import os
import glob
from PIL import Image
import pickle
def get_input_names():
	#list=glob.glob('~/data/ISIC2018_Task1-2_Training_Input/*jpg')	
	list1=glob.glob('/users/PAS0272/osu10258/data/ISIC2018_Task1-2_Training_Input/*jpg')
	return list1

def get_groundtruth_names():
	list=glob.glob('~/data/ISIC2018_Task1-2_Training_Input/*png')	
	return list

def convert_name_ground_truth(names_list):
	a1=[]
	for name in names_list:
		whole_name=[]
		string1=name[61:73]
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task1-2_Training_Input/'+string1+'.jpg')
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task2_Training_GroundTruth_v3/'+string1+'_attribute_globules.png')
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task2_Training_GroundTruth_v3/'+string1+'_attribute_milia_like_cyst.png')
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task2_Training_GroundTruth_v3/'+string1+'_attribute_negative_network.png')
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task2_Training_GroundTruth_v3/'+string1+'_attribute_pigment_network.png')
		whole_name.append('/users/PAS0272/osu10258/data/ISIC2018_Task2_Training_GroundTruth_v3/'+string1+'_attribute_streaks.png')
		a1.append(whole_name)		
	return a1
	
def analysis(whole_name):
	a2=[]
	for count1,name in enumerate(whole_name):
		a1=[]
		for count,name_1 in enumerate(name):
			if(count==0):
				a1.append(0)
				continue	
			image_path=name_1
			image=Image.open(image_path)
			width,height=image.size
			flag=0
			pixels=image.load()
			for i in range(width):
				for j in range(height):
					if(pixels[i,j]==255):
						flag=1
			a1.append(flag)
		a2.append(a1)
		print(count1)
	return a2
			
def main():
	names=get_input_names()
	#print (names)
	whole_names=convert_name_ground_truth(names)
#	with open("~/a3.pickle","wb") as f:
#		pickle.dump(whole_names,f)

	with open("/users/PAS0272/osu10258/data/a3.pickle","wb") as f:
		pickle.dump(whole_names,f)
	#whole_names.to_pickle('~/a2')
	name_analysis=analysis(whole_names)	
	print (name_analysis)
	with open("/users/PAS0272/osu10258/data/a2.pickle","wb") as f:
		pickle.dump(name_analysis,f)
	#name_analysis.to_pickle('~/a1')	
	
		

if __name__ == "__main__":
	main()
