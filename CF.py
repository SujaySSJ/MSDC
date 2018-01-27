# import pandas as pd 

# history=pd.read_csv("three_tup.csv",sep=",",names=["userID","songID","playcount"])
# ratingMat=history.pivot(columns='userID',index='songID',values='playcount')
# ratingMat=ratingMat.fillna(0)

# R=ratingMat.values
# print(history.head())
# print(ratingMat.values)
import random
import sys

no_of_users=4
no_of_songs=5
no_of_ratings=13
features=5

dataset_path="testrating.txt"
#randomly initialising user and song matrices

user_pref_matrix=[[random.random() for i in range(features)] for j in range(no_of_users)]
song_feat_matrix=[[random.random() for i in range(features)] for j in range(no_of_songs)]

error_list=[]
#error_per_iteration=0

def getRating(userID,songID):
	return sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(features)])

def learnFeatures(steps=10000,error_conv=0.001,alpha=0.0001,beta=0.02):
	for iteration in xrange(steps):
		with open(dataset_path,'r') as dataset:
			for triplet in dataset:
				userID,songID,rating=triplet.split("\t")
				userID,songID,rating=int(userID),int(songID),int(rating)
				error=float(rating)-getRating(int(userID),int(songID))
				#error_per_iteration+=error
				for f in xrange(features):
					user_pref_matrix[userID][f]+=alpha*(2*error*song_feat_matrix[songID][f]-beta*user_pref_matrix[userID][f])
					song_feat_matrix[songID][f]+=alpha*(2*error*user_pref_matrix[userID][f]-beta*song_feat_matrix[songID][f])
				
		# error_list+=error_per_iteration/no_of_ratings
		# error_per_iteration=0
		sys.stdout.write("\rIterations done: "+str(iteration))

learnFeatures()
R=[[i for i in range(no_of_users)] for j in range(no_of_songs)]
for i in xrange(no_of_songs):
	for j in xrange(no_of_users):
		R[i][j]=getRating(j,i)
print(R)

