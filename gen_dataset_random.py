import random
import csv
from numpy import genfromtxt

data_set=[]# schema 0==>user_id 1==>song_id 2==>play_count 3==>normalised rating

for i in range(1,91):
	data_set.append([])

cell=0

op=open('three_tup.csv','wb')

op2=open('data_set_with_rating.csv','wb')
wr=csv.writer(op,dialect='excel')

wr2=csv.writer(op2,dialect='excel')

for user in range(0,6):
	for song in range(0,15):
		data_set[cell].append(user+1)
		data_set[cell].append(song+1)
		rnd_for_zero=random.randint(0,5)
		if(rnd_for_zero >2):
			data_set[cell].append(random.randint(1,100))#playcount min:0 max:100 
		else:
			data_set[cell].append(0)
		
		if(data_set[cell][2] >0 and data_set[cell][2]<=20):
			data_set[cell].append(1)

		if(data_set[cell][2] >20 and data_set[cell][2]<=40):
			data_set[cell].append(2)

		if(data_set[cell][2] >40 and data_set[cell][2]<=60):
			data_set[cell].append(3)

		if(data_set[cell][2] >60 and data_set[cell][2]<=80):
			data_set[cell].append(4)

		if(data_set[cell][2] >80 and data_set[cell][2]<=100):
			data_set[cell].append(5)

		wr.writerow(data_set[cell][:3])#writes only 3 tuples!
		wr2.writerow(data_set[cell])
		cell=cell+1


# def read_data():
# 	with open('data_set_with_rating.csv','r') as file:
# 		reader=csv.reader(file,delimiter=',')
# 		my_data=list(reader)

# 	return my_data

def gen_matrix():
	#dataset=read_data()
	dataset=data_set
	matrix=[]
	for song in range(1,16):
		temp=[]
		for row in dataset:
			if ((row[1])==song):
				if(row[2]==0):
					temp.append(0)
				else:
					temp.append((row[3]))
		matrix.append(temp)
	return matrix		


#print(gen_matrix())
