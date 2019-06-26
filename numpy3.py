import numpy as np
a=np.array([[1,2,3],[3,4,5]])
np.savetxt('a2.txt',a)
np.loadtxt('a2.txt')


import numpy as np
c=np.loadtxt('a2.txt')
print(c.reshape(3,2))
