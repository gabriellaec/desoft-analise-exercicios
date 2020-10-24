with open('macacos-me-mordam.txt','r') as arq:
    x=arq.read()
t=x.upper().split()
c=0
for i in range(len(t)):
    if t[i]=='BANANA':
        c+=1
print(c)




    
