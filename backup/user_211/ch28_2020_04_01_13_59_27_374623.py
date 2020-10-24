import math
l=[0]*100
l[0]=1
i=1
for i<len(l):
    soma=math.sum(1/(2**i))
    i+=1
print soma
