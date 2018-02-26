import random
import sys
import numpy
import pickle
import matplotlib.pyplot as plt
import time

#make changes to the following parameters as per each dataset
#total no of unique users in dataset
no_of_users=110000

#total no of unique songs in dataset
no_of_songs=180000

#total no of tuples in dataset
no_of_ratings=1365272

#total no of features per vector
no_of_features=10

no_of_iterations=200

#name of the training dataset
dataset_path="db_110_indexed_with_rating.txt"#"final_db_150.txt"

errorlist_path="errorlist_content.pickle"
user_pref_path="user_pref_matrix_110k.pickle"
song_feat_path="song_feat_matrix_merged.pickle"
errorlist_file_path="errorlist_content.txt"

#loading user and song vectors
with open(user_pref_path,'rb') as file:
	user_pref_matrix=pickle.load(file)
with open(song_feat_path,'rb') as file:
	song_feat_matrix=pickle.load(file)



def getRating(userID,songID):
	return sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(no_of_features)])

def readFile():
	with open(dataset_path,'r') as dataset:
		for triplet in dataset:
			entire_file.append(triplet.split("\t"))

# Will return two matrices user pref and song features
# change parameters as per requirement

def learnFeatures(user_pref_matrix,song_feat_matrix,steps=200,error_conv=0.001,alpha=0.01,beta=0.01):
	
	error_list=[]
	error_per_iteration=0
	error=0
	count=0
	entire_file=[]
	errorlist_file=open(errorlist_file_path,'w')
	print("Loading dataset into memory")
	with open(dataset_path,'r') as dataset:
		for triplet in dataset:
			line=triplet.split("\t")
			entire_file.append([int(line[0]),int(line[1]),float(line[3])])

	print("Beginning Training on {}\n.\n.".format(dataset_path))
	print("Total user vectors {}, Total song vectors {} ,Total Ratings {}\nFeatures per vector {}".format(no_of_users,no_of_songs,no_of_ratings,no_of_features))
	print("Total iterations to be done {}\n.\n.".format(steps))
	

	for iteration in range(steps):
		for line in entire_file:
			#change the index for rating as per the position it occurs in line
			userID,songID,rating=line[0],line[1],line[2]
				
			error=rating-sum([user_pref_matrix[userID][i]*song_feat_matrix[songID][i] for i in range(no_of_features)])
				
			#adding squared error
			error_per_iteration+=error*error

			#updating weights
			for f in range(no_of_features):

				u=user_pref_matrix[userID][f]
				s=song_feat_matrix[songID][f]

				user_pref_matrix[userID][f]=u+alpha*(2*error*s-beta*u)
				#song_feat_matrix[songID][f]=s+alpha*(2*error*u-beta*s)

				
			count=count+1

			#Displaying Progress
			sys.stdout.write("\rIteration "+str(iteration+1)+" Percent Done :"+str(round(float(count)*100/(no_of_ratings*no_of_iterations),4)))
	
		#count=0
		error_list.append(round(error_per_iteration/(2*no_of_ratings),5))
		errorlist_file.write(str(iteration+1)+","+str(error_list[-1])+"\n")
		error_per_iteration=0
		error=0
	print("\n")

	#saving error list
	with open(errorlist_path,'wb') as file:
		pickle.dump(error_list,file)
	errorlist_file.close()
	

	return user_pref_matrix,song_feat_matrix



start_time=time.time()

user_pref_matrix,song_feat_matrix=learnFeatures(user_pref_matrix,song_feat_matrix,steps=no_of_iterations)

total_time=time.time()-start_time

#dumping the matrices for later use
#numpy.save(user_pref_path,user_pref_matrix)
#numpy.save(song_feat_path,song_feat_matrix)
with open('user_pref_matrix_final.pickle','wb') as file:
	pickle.dump(user_pref_matrix,file)
# with open(song_feat_path,'wb') as file:
# 	pickle.dump(song_feat_matrix,file)


print("\nErrors for every iteration saved in {} (as python list)\nUser Pref Vectors saved as {} (as python list)\nSong Feature Vectors saved as {} (as python list)".format(errorlist_path,user_pref_path,song_feat_path))
print("\n\nTraining Complete in {} seconds.".format(total_time))


#loading the error file
with open(errorlist_path,'rb') as file:
	error_list=pickle.load(file)
with open('userMapping110k.pickle','rb') as file:
	userMapping110k=pickle.load(file)

user_pref_dict={}
for key,value in userMapping110k.items():
	user_pref_dict[key]=user_pref_matrix[value]

with open('user_pref_dict.pickle','wb') as file:
	pickle.dump(user_pref_dict,file)

#plotting error per iteration vs iteration
print("\nDisplaying Error graph")

plt.plot(list(range(no_of_iterations)),error_list)
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.show()