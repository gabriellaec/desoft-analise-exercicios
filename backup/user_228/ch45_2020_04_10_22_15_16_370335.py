lista=[]
c=True
while c:
    a=int(input("manda numeros inteiros positivos ae bundao"))
    if a==0 or a<0:
        c=False
    else:
        lista.append(a)
        
    i=len(lista)-1
    while i>=0:
          print (lista[i])
              i-=1

        
    
    
          