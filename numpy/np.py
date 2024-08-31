import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)

#get dimention
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
print(b.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#get total size
print(a.nbytes)
print(b.nbytes)

#get a specific element
print(b[1,1])

#get a specific row
print(b[0,:])

#get a specific colum
print(b[:,2])

#get a littel fancy[startindex:endindex:stepsize]
print(b[0, 0:2:1])

#3D example
e = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(e)

#get a saecific element(work outside in)
print(e[0,0,1])

#Replace
e[0,:,:]=[[11,12],[13,14]]
print(e)

#All zero matrix
r=np.zeros((2,3))
print(r)
t=np.zeros((2,3))
print(t)

#All ones matrix
y=np.ones((4,2,2), dtype='int32')
print(y)

#Any another number
u=np.full((2,2), 99, dtype='float32')
print(u)

#Any other number (full_like)
print(np.full_like(b, 4))

#Random decimal number
print(np.random.rand(5,6))

#Random integer values
n=np.random.randint(100, size=(2,6))
print(n)

#Identity matrix
m=np.identity(4)
print(m)

#Repeat an array
arr=np.array([[1,2,3],[4,5,6]])
r1=np.repeat(arr,3, axis=0)
print(r1)

#
output=np.ones((5,5))
print(output)
v=np.zeros((3,3))
v[1,1]=9
print(v)
output[1:4,1:4]=v
print(output)
