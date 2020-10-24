n=[]
a=int(input('digite um número: '))
while a>0:
    n.append(a)
    a=int(input('digite um número: '))
r=[]
i=len(n)-1
while i>=0:
    r.append(n[i])
    i-=1
    
print(r)