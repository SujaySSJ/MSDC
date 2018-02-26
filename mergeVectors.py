import pickle
from collections import defaultdict

with open('song_feat_matrix_250.pickle','rb') as file:
	song_feat_matrix_250=pickle.load(file)
with open('songMapping250.pickle','rb') as file:
	songMapping250=pickle.load(file)
with open('songMapping110k.pickle','rb') as file:
	songMapping110k=pickle.load(file)
with open('song_feat_matrix_110k.pickle','rb') as file:
	song_feat_matrix_110k=pickle.load(file)

song_feat_matrix_110k=song_feat_matrix_110k[:-2]
song_feat_matrix_250=song_feat_matrix_250[:-1]

song_feat_dict={}
for key,value in songMapping110k.items():
	song_feat_dict[key]=song_feat_matrix_110k[value]
for key,value in songMapping250.items():
	song_feat_dict[key]=song_feat_matrix_250[value]

c=0
for key,value in songMapping110k.items():
	if key in songMapping250:
		song_feat_matrix_110k[value]=song_feat_matrix_250[songMapping250[key]]
		c=c+1
with open('song_feat_dict.pickle','wb') as file:
	pickle.dump(song_feat_dict,file)

with open('song_feat_matrix_merged.pickle','wb') as file:
	pickle.dump(song_feat_matrix_110k,file)

print(c)
print(len(song_feat_dict))
