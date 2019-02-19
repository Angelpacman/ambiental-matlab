#%hecho por Jose Angel Resendiz Aviles
import numpy as np

A= np.array([np.arange(1,8,1),np.arange(2,15,2),np.arange(21,0,-3),np.arange(5,36,5)])
A
B = np.array( [A[[0],[0,2,4,6]],  A[[2],[0,2,4,6]],  A[[3],[0,2,4,6]]  ])
B
a=A[2,:]
a

b=A[:,4], A[:,6]
b = np.ravel(b)
b = b.reshape(8,1)
b

bb=b.reshape(1,8)
bb

u=np.array([a,b])
u = np.ravel(u)
u
