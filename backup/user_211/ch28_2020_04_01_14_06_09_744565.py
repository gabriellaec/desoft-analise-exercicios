l=[0]*100
l[0]=1
i=1

while i<len(l):
    l[i]=(1/(2**i))
    i=i+1
soma=sum(l)
print(soma)
