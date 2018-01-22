import pandas as pd 

data=pd.read_csv("all_details_mod.csv",sep=",",header=None)
data.columns=["index","userID","playCount"]



# data["userID"]=data["userID"].str.replace("user:","")
# data["playCount"]=data["playCount"].str.replace("song-count:","")
data["playCount"]=data["playCount"].astype(int)
# data.to_csv('all_details_mod.csv',sep=",")
# dataFreq=data.userID.value_counts()
# dataFreq=data.groupby('userID').count()
#print(dataFreq)


data=data.drop('index',axis=1)

# print(data.head())
# print(data.dtypes)

data20=data[data['playCount']>=20]
data20.to_csv("usersGreaterThan20Songs.csv",sep=",")

data50=data[data['playCount']>=50]
data50.to_csv("usersGreaterThan50Songs.csv",sep=",")

data100=data[data['playCount']>=100]
data100.to_csv("usersGreaterThan100Songs.csv",sep=",")

data150=data[data["playCount"]>=150]
data150.to_csv("usersGreaterThan150Songs.csv",sep=",")

data200=data[data["playCount"]>=200]
data200.to_csv("usersGreaterThan200Songs.csv",sep=",")

#print("Greater than 20 :",data20.shape[0])
# print("Greater than 50 :",data50.shape[0])
# print("Greater than 150 :",data150.shape[0])
#data.to_csv('all_details_mod.csv',sep=",")
#print(data.userID.value_counts())

