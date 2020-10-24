lista=[]
x=0
lista.append(input('Digite uma palavra: '))
while lista[x]!='Fim':
    x+=1
    lista.append(input('Digite uma palavra: '))        	            
i=0
n=len(lista)
while i<n:
    if lista[i][0]=='a':
        print(lista[i])
        i+=1
    else:
        i+=1
    
    
                      
                          