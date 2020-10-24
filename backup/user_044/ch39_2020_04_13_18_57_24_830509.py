for i in range(0,1000,1):
    n=i
    ls=[0,1]
    lista=[]
    lista.clear()
    while n!=1:
        if n%2==0:
            n=n/2
            lista.append(n)
        else:
            n=3*n+1
            lista.append(n)
    ls.append(len(lista))       
for i in range(len(ls)):
    y=0
    if lista[i]>y:
        y=i
print(y)
        
            
    
    