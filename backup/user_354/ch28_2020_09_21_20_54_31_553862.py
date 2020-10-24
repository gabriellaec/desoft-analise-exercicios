import math
i=0
f[0]=1
while (i<100):
    f[i]=f[i-1]*1/2
print(math.soma(f[0],f[99]))