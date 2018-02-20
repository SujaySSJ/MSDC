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
#user_pref_matrix=[[random.random() for i in range(no_of_features)]for j in range(no_of_users)]
#song_feat_matrix=[[random.random() for i in range(no_of_features)]for j in range(no_of_songs)]

def readFileDict(filename):
	file_dict={}
	with open(filename) as file:
		for line in file:
			triplet=line.split("\t")
			file_dict[int(triplet[1])].append([int(triplet[0]),float(triplet[1])])
	print(file_dict[:5])

readFileDict(dataset_path)