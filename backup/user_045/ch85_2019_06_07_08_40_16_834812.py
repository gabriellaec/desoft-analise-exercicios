with open('macacos-me-mordam.txt','r') as arquivo:
    r = arquivo.readlines() 
c=0
r=r.split()
for e in r:
    g=e.lower()
    if g =='banana':
        c+=1
print(c)