import pickle
list1=pickle.load(open("/users/PAS0272/osu10258/data/a2.pickle","rb"))
#print (list1)
list2=pickle.load(open("/users/PAS0272/osu10258/data/a3.pickle","rb"))
#print (list2[449])
#print (list2[2588])
print (list1)

count_total=[0,0,0,0,0]
for index1,list1s in enumerate(list1):
	count=0
	for list2s in list1s:
		count+=list2s
	if (count==3):
		print(index1)
		break
print(list2[14])
print(list1[14])
