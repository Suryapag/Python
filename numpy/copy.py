import numpy as np


#Be careful when coping arrays!!!
a=np.array([1,2,3]) 
b=a.copy()
b[0]=100
print(b,a)

# +,-,* using in array
a2=np.array([1,2,3,4])
print(a2+1)

#Take a sin value
print(np.cos(a))

#Linear Algebra
al=np.ones((2,3))
print(al)
bl=np.full((3,2),2)
print(bl)
print(np.matmul(al,bl))

#find the determinant
c=np.identity(3)
print(np.linalg.det(c))
