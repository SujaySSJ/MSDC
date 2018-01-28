import random
import sys
import numpy
import pickle
import matplotlib.pyplot as plt
import time

#make changes to the following parameters as per each dataset
#total no of unique users in dataset
no_of_users=51308

#total no of unique songs in dataset
no_of_songs=325180

#total no of tuples in dataset
no_of_ratings=12120030

#total no of features per vector
no_of_features=2

#name of the training dataset
dataset_path="final_db_150.txt"#"testrating.txt"

errorlist_path="errorlist.pickle"
user_pref_path="user_pref_matrix"
song_feat_path="song_feat_matrix"

#randomly initialising user and song matrices
user_pref_matrix=numpy.random.rand(no_of_users,no_of_features)
song_feat_matrix=numpy.random.rand(no_of_songs,no_of_features)


def getRating(userID,songID):
	return sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(features)])

# Will return two matrices user pref and song features
# change parameters as per requirement

def learnFeatures(user_pref_matrix,song_feat_matrix,steps=10000,error_conv=0.001,alpha=0.002,beta=0.02):
	song_feat_matrix=song_feat_matrix.T
	error_list=[]
	error_per_iteration=0
	error=0
	count=0
	print("Beginning Training on {}\n.\n.".format(dataset_path))
	print("Total user vectors {}, Total song vectors {} ,Total Ratings {}\nFeatures per vector {}".format(no_of_users,no_of_songs,no_of_ratings,no_of_features))
	print("Total iterations to be done {}\n.\n.".format(steps))
	
	for iteration in xrange(steps):
		with open(dataset_path,'r') as dataset:
			for triplet in dataset:
				line=triplet.split("\t")
				
				#change the index for rating as per the position it occurs in line
				userID,songID,rating=int(line[0]),int(line[1]),float(line[3])
				
				error=rating-numpy.dot(user_pref_matrix[userID,:],song_feat_matrix[:,songID])
				
				#adding squared error
				error_per_iteration+=error*error

				#updating weights
				for f in xrange(no_of_features):
					user_pref_matrix[userID][f]+=alpha*(2*error*song_feat_matrix[f][songID]-beta*user_pref_matrix[userID][f])
					song_feat_matrix[f][songID]+=alpha*(2*error*user_pref_matrix[userID][f]-beta*song_feat_matrix[f][songID])
				
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
	

	return user_pref_matrix,song_feat_matrix.T

start_time=time.time()

user_pref_matrix,song_feat_matrix=learnFeatures(user_pref_matrix,song_feat_matrix,steps=1)

total_time=time.time()-start_time

#dumping the matrices for later use
numpy.save(user_pref_path,user_pref_matrix)
numpy.save(song_feat_path,song_feat_matrix)



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