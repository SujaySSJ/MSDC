import random
import sys
import numpy
import pickle
import matplotlib.pyplot as plt
import time

#make changes to the following parameters as per each dataset
#total no of unique users in dataset
no_of_users=110000#51308

#total no of unique songs in dataset
no_of_songs=180000#325180

#total no of tuples in dataset
no_of_ratings=1450934#12120030

#total no of features per vector
no_of_features=10

#name of the training dataset
dataset_path="db_110k_indexed.txt"#"final_db_150.txt"

errorlist_path="errorlist.pickle"
user_pref_path="user_pref_matrix.pickle"
song_feat_path="song_feat_matrix.pickle"

#randomly initialising user and song matrices
user_pref_matrix=[[random.random() for i in range(no_of_features)]for j in range(no_of_users)]
song_feat_matrix=[[random.random() for i in range(no_of_features)]for j in range(no_of_songs)]


def getRating(userID,songID):
	return sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(no_of_features)])

def readFile():
	with open(dataset_path,'r') as dataset:
		for triplet in dataset:
			entire_file.append(triplet.split("\t"))

# Will return two matrices user pref and song features
# change parameters as per requirement

def learnFeatures(user_pref_matrix,song_feat_matrix,steps=10000,error_conv=0.001,alpha=0.0002,beta=0.001):
	
	error_list=[]
	error_per_iteration=0
	error=0
	count=0
	entire_file=[]
	with open(dataset_path,'r') as dataset:
		for triplet in dataset:
			line=triplet.split("\t")
			entire_file.append([int(line[0]),int(line[1]),float(line[2])])
	print("Beginning Training on {}\n.\n.".format(dataset_path))
	print("Total user vectors {}, Total song vectors {} ,Total Ratings {}\nFeatures per vector {}".format(no_of_users,no_of_songs,no_of_ratings,no_of_features))
	print("Total iterations to be done {}\n.\n.".format(steps))
	

	for iteration in xrange(steps):
		for line in entire_file:
			#change the index for rating as per the position it occurs in line
			userID,songID,rating=line[0],line[1],line[2]
				
			error=rating-sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(no_of_features)])
				
			#adding squared error
			error_per_iteration+=error*error

			#updating weights
			for f in xrange(no_of_features):
				#user_pref_matrix[userID][f]+=alpha*(2*error*song_feat_matrix[f][songID]-beta*user_pref_matrix[userID][f])
				#song_feat_matrix[f][songID]+=alpha*(2*error*user_pref_matrix[userID][f]-beta*song_feat_matrix[f][songID])
				u=user_pref_matrix[userID][f]
				s=song_feat_matrix[songID][f]

				user_pref_matrix[userID][f]=u+alpha*(2*error*s-beta*u)
				song_feat_matrix[songID][f]=s+alpha*(2*error*u-beta*s)

				
			count=count+1

			#Displaying Progress
			sys.stdout.write("\rIteration "+str(iteration+1)+" Percent Done :"+str(round(float(count)*100/no_of_ratings,4)))

	
		count=0
		error_list.append(round(error_per_iteration/2*no_of_ratings,5))
		error_per_iteration=0
		error=0
	print("\n")

	#saving error list
	with open(errorlist_path,'wb') as file:
		pickle.dump(error_list,file)
	

	return user_pref_matrix,song_feat_matrix

start_time=time.time()

user_pref_matrix,song_feat_matrix=learnFeatures(user_pref_matrix,song_feat_matrix)

total_time=time.time()-start_time

#dumping the matrices for later use
#numpy.save(user_pref_path,user_pref_matrix)
#numpy.save(song_feat_path,song_feat_matrix)
with open(user_pref_path,'wb') as file:
	pickle.dump(user_pref_matrix,file)
with open(song_feat_path,'wb') as file:
	pickle.dump(song_feat_matrix,file)


print("\nErrors for every iteration saved in {} (as python list)\nUser Pref Vectors saved as {}.npy (as numpy array)\nSong Feature Vectors saved as {}.npy (as numpy array)".format(errorlist_path,user_pref_path,song_feat_path))
print("\n\nTraining Complete in {} seconds.".format(total_time))

#example to load save npy arrays back
#a=numpy.load(user_pref_path+".npy")
#b=numpy.load(song_feat_path+".npy")
# print(user_pref_matrix)
# print(song_feat_matrix)


#loading the error file
with open(errorlist_path,'r') as file:
	error_list=pickle.load(file)

#plotting error per iteration vs iteration
print("\nDisplaying Error graph")

plt.plot(list(range(10000)),error_list)
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()