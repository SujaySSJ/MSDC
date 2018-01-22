import pandas as pd 

history=pd.read_csv("three_tup.csv",sep=",",names=["userID","songID","playcount"])
ratingMat=history.pivot(columns='userID',index='songID',values='playcount')
ratingMat=ratingMat.fillna(0)

R=ratingMat.values
print(history.head())
print(ratingMat.values)
