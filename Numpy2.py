import numpy as np
i=np.empty([8,2])
a=np.arange(100,200,5)
j=len(a)
while j<=16 :
  i=i+a
i.reshape(8,2)
i
