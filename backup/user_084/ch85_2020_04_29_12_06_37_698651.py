with open('macacos-me-mordam.txt','r') as arq:
    x=upper(arq.read)
a=x.split()
c=0
for i in range(len(a)):
    if a[i]==BANANA:
        c+=1
print(c)
    
