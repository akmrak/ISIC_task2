from PIL import Image
import pickle
def analysis(whole_name):
	a2=[]
	for count1,name in enumerate(whole_name):
		print (count1)
		for count,name_1 in enumerate(name):
				
			image_path=name_1
			image=Image.open(image_path)
			width,height=image.size
			flag=0
			#pixels=image.load()
			list_pixels=list(image.getdata())
			
			if(count==0):
				#print ("count0")
				#print (name_1)
				continue
			elif(count==1):
				#print ("count1")
				#print (name_1)
				sum_images=list_pixels[:]	
			else:
				#print ("count2")
				#print (name_1)
				sum_images=[sum(x) for x in zip(sum_images,list_pixels)]
		count_pixel=0	
		#print (len(sum_images))
		for i in range(len(sum_images)):
			if(sum_images[i]>255):
				count_pixel+=1
		a2.append(count_pixel)
	return a2

def main():
	list2=pickle.load(open("/users/PAS0272/osu10258/data/a3.pickle","rb"))
	#list2=list2[:100]	
	a2=analysis(list2)
	with open("/users/PAS0272/osu10258/data/test_overlap_data.pickle","wb") as f:
		pickle.dump(a2,f)
	print (a2)
		

if __name__ == "__main__":
	main()
