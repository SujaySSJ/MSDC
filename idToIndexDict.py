import sys

#import pandas as pd
#import json
import pickle
#year1_valid_triplets_visible.txt
dataset_path="year1_valid_triplets_visible.txt"#"testdataset.txt"
new_dataset_path="newtestdatsset.txt"
user_mapping_path="userMapping.txt"
song_mapping_path="songMapping.txt"

userMapping=open(user_mapping_path,'w')
newDataset=open(new_dataset_path,'w')
#songMapping=open(song_mapping_path,'w')

userID=""
prevID=""
userIndex=0
songIndex=0
songDict={}

with open(dataset_path) as fp:
	while True:
		triplet=fp.readline().split('\t')

		if triplet[0]=='':
			break

		userID=triplet[0]

		if userID!=prevID:
			userMapping.write(triplet[0]+'\t'+str(userIndex)+'\n')
			prevID=userID
			userIndex=userIndex+1
			sys.stdout.write("\r"+"No. of user ids changed : "+str(userIndex)+" No. of song ids changed : "+str(songIndex))

		if triplet[1] not in songDict:
			songDict[triplet[1]]=songIndex
			songIndex=songIndex+1

		#newDataset.write(str(userIndex)+'\t'+triplet[1]+'\t'+triplet[2])
		newDataset.write(str(userIndex-1)+'\t'+str(songDict[triplet[1]])+'\t'+triplet[2])

	print("\nUser IDs replaced\nWritten to userMapping.txt.\nNew Dataset is formed")	

userMapping.close()
newDataset.close()

with open('songMapping.pickle', 'wb') as file:
	pickle.dump(songDict,file)


# print("Now replacing song ids")

# df=pd.read_csv(new_dataset_path,sep="\t",header=None)
# df.columns=["userID","songID","playcount"]

# songMapping=[]
# i=0
# for songID in df.songID.unique():
# 	df.loc[df.songID==songID,'songID']=i
# 	songMapping.append([songID,i])
# 	i=i+1
# 	sys.stdout.write("\r"+"No. of song ids changed : "+str(i))
# print("\nSong IDs replaced")
# pd.DataFrame(songMapping,columns=["songID","index"]).to_csv(song_mapping_path,sep="\t",index=False)
# df.to_csv(new_dataset_path,index=False,sep="\t")
