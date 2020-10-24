lista=[]
x=0
lista.append(input('Digite uma palavra: '))
while(lista[x]!='Fim'):
             lista.append(input('Digite uma palavra: '))
             x = x + 1	            
x=0
a=len(lista)
while x<=a:
    if lista[x][0]=='a':
        print(lista[x])
        x+=1
    else:
        x+=1
    
    
                      
                          