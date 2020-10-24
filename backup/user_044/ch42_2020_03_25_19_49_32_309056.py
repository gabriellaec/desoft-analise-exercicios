lista=[]
x=0
lista.append(input('Digite uma palavra: '))
while lista[x]!='Fim':
    lista.append(input('Digite uma palavra: '))
    x = x + 1
             	            
i=0
a=len(lista)
while i<a:
    if lista[i][0]=='a':
        print(lista[i])
        i+=1
    else:
        i+=1
    
    
                      
                          