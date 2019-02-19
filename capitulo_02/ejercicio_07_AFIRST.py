#%hecho por Jose Angel Resendiz Aviles
import numpy as np

Afirst = np.arange(4,50,3)
Asecond = np.array([Afirst[:4], Afirst[12:] ]) #, Afirst[12:16]

Afirst
Asecond = Asecond.reshape(8,1)
Asecond.shape
Asecond
