from amth import *
import numpy as np
listaang=np.arange(0,91,1)
seno=[]
for i in range(len(listaang)):
    x=sin(radians(i))
    y=4*i*(180-i)/(40500-i*(180-i))
    seno.append(abs(x-y))
print(max(seno))
    
    