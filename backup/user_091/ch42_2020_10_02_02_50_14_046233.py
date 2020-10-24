lista=[]
while True:
    x=input('Digite sua palavra: ')
    if x== 'fim':
        break
    lista.append(x)

lista_novo=[]   
i=0
while i<len(lista):
    if lista[i][0]=='a' or lista[i][0]=='A':
        lista_novo.append(lista[i])
        print(lista_novo[i])
        i+=1
    else:
        None
        i+=1

                          
    

    
    
