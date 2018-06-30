from sklearn import preprocessing
import pickle
import numpy as np 
import cv2
import h5py
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
input_name="/users/PAS0272/osu10258/data/a3.pickle"
input_label="/users/PAS0272/osu10258/data/a2.pickle"
def load_image_names():
	return pickle.load(open(input_name,"rb"))
def image_to_feature_vector(image, size=(32, 32)):
	return cv2.resize(image,size).flatten()
def load_data_images(list_names):
	images=[]
	
	for count,name in enumerate(list_names):
		image=cv2.imread(name)
		image=image_to_feature_vector(image,(224,224))
		image_mean=np.mean(image)
		#basic normalization
		image=image/image_mean
		images.append(image)
	return images	
	
def load_data_labels(i):
	labels_all=pickle.load(open(input_label,"rb"))
	label_0=[a[i+1] for a in labels_all]		
	return label_0
def svm_classifier(data,labels):
	le = preprocessing.LabelEncoder()
	print("[INFO] constructing training/testing split...")
	(trainData,testData,trainLabels,testLabels)=train_test_split(data,labels,test_size=0.25,random_state=42)
	print("[INFO] training Linear SVM classifier...")
	model = LinearSVC()
	model.fit(trainData, trainLabels)
	print("[INFO] evaluating classifier...")
	predictions = model.predict(testData)
	print(classification_report(testLabels, predictions,target_names=['0','1']))
		
def main():
	list1=load_image_names()
	list_names=[a[0] for a in list1]
	load_images=load_data_images(list_names)
	for i in range(5):
		print(i+1,"attribute classifier starts")	
		load_labels=load_data_labels(i)
		#load_labels=load_labels[:10]
		#print(load_images[0].shape,load_labels)		
		svm_classifier(load_images,load_labels)	
		print(i+1,"attribute classifier ends")	

if __name__ == "__main__":
	main()
