#%hecho por Jose Angel Resendiz Aviles
import numpy as np

C = np.array([np.arange(2,11,2), np.arange(3,16,3), np.arange(7,36,7)] )
C

ua=C[:,2]
ua = ua.reshape(1,3)
ua

ub=C[1,:]
ub
bb = ub.T #np.transpose(ub)
bb

uc=np.array([C[:,0],C[:,2],C[:,4]])
uc = np.ravel(uc)
uc
ud=np.array([C[0,:], C[1,:]])
ud = np.ravel(ud)
ud
bb=ud
bb = bb.reshape(10,1)
bb
