#%hecho por Jose Angel Resendiz Aviles
import numpy as np

A=np.eye(7,7)

A
A[0:2,0:3]=2
A
A[2:3,0:3]=3
A
A[4:7,0:2]=4
A
A[4:7,2:3]=7
A
A[0:3,4:7]=5
A
A[4:7,4:7]=9
A
