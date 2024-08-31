import numpy as np

stat = np.array([[7,2,3],[4,5,6]])
print(stat)
print(np.min(stat))
print(np.max(stat, axis=1))
print(np.sum   (stat))

#reshape
before=np.array([[1,2,3,4],[5,6,7,8]])
print(before.reshape(2,2,2))

#Vertically stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))

#Horizontal stack
h1=np.ones((2,4))
h2=np.zeros((2,2))
print(np.hstack([h1,h2]))

#load data from file
#file=np.genfromtxt('data.txt', delimiter=',')
#file.astype('int32')
#print(file)

#Boolean masking and advanced indexing
