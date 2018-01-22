# import pandas as pd 

# history=pd.read_csv("three_tup.csv",sep=",",names=["userID","songID","playcount"])
# ratingMat=history.pivot(columns='userID',index='songID',values='playcount')
# ratingMat=ratingMat.fillna(0)

# R=ratingMat.values
# print(history.head())
# print(ratingMat.values)
import random

no_of_users=
no_of_songs=
features=

dataset_path=
#randomly initialising user and song matrices

user_pref_matrix=[[random.random() for i in range(features)] for j in range(no_of_users)]
song_feat_matrix=[[random.random() for i in range(features)] for j in range(no_of_songs)]

def getRating(userID,songID):
	return sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(features)])

def learnFeatures(steps,error_conv,alpha,beta):
	for iteration in xrange(steps):
		with open(dataset_path,'r') as dataset:
			for triplet in dataset:
				userID,songID,rating=triplet.split("\t")
				error=rating-getRating(int(userID),int(songID))
				for f in xrange(features):
					user_pref_matrix[userID][f]+=alpha*(2*error*song_feat_matrix[songID][f]-beta*user_pref_matrix[userID][f])
					song_feat_matrix[songID][f]+=alpha*(2*error*user_pref_matrix[userID][f]-beta*song_feat_matrix[songID][f])
				



