with open('macacos-me-mordam.txt','r') as arq:
    x=arq.read
b=x.upper()
a=b.split()
c=0
for i in range(len(a)):
    if a[i]==BANANA:
        c+=1
print(c)
    
