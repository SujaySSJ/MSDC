import numpy
#import gen_dataset_random



def getFeatures(R,U,S,K,steps=1000,alpha=0.002,beta=0.02):
	S=S.T
	for step in xrange(steps):
		for i in xrange(len(R)):
			for j in xrange(len(R[i])):
				if R[i][j]>0:
					error=R[i][j]-numpy.dot(U[i,:],S[:,j])
					for k in xrange(K):
						U[i][k]=U[i][k]+alpha*(2*error*S[k][j]-beta*U[i][k])
						S[k][j]=S[k][j]+alpha*(2*error*U[i][k]-beta*S[k][j])

	
	return U,S.T	


def getRecommendations(R,nR,user,N=1):
	nrlist={}
	for i in range(len(R)):
		if R[i][user]<=0:
			nrlist[i]=nR[i][user]
	return sorted(nrlist, key=nrlist.get, reverse=True)[:N]
	



R=[
	[5,3,0,1],
	[4,0,0,1],
	[1,1,0,5],
	[1,0,0,4],
	[0,1,5,4]
	]
#R=gen_dataset_random.gen_matrix()
R=numpy.array(R)
N=len(R)
M=len(R[0])
K=2
U=numpy.random.rand(N,K)
S=numpy.random.rand(M,K)

nU,nS=getFeatures(R,U,S,K)
nR=numpy.dot(nU,nS.T)
print("Original Rating Matrix:")
print(R)
print("Learnt Rating Matrix:")
print(nR)
for i in range(M):
	recList=getRecommendations(R,nR,i,N)
	if recList:
		print("Songs Recommended for User"+str(i+1))
		for j in range(len(recList)):
			print("Song No.:"+str(recList[j]+1)+" , Rating:"+str(nR[recList[j]][i]))

