#%hecho por Jose Angel Resendiz Aviles
import numpy as np
A = np.array([[6, 43, 2, 11, 87],[12, 6, 34, 0, 5],[34, 18, 7, 41, 9]])
A
va = A[1,:]
va

vb = A[:,3]
vb =np.transpose(vb)
vb
vc = np.array([A[0,:] , A[1,:]])
vc
#vc = vc.reshape(1,10)
vc = np.ravel(vc)
vc

vd = np.array([A[:,1] , A[:,4]])
vd = np.ravel(vd)
vd
