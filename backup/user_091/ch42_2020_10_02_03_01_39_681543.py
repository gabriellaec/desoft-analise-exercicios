lista=[]
while True:
    x=input('Digite sua palavra: ')
    if x== 'fim':
        break
    lista.append(x)

lista_novo=[]   
i=0
while i<len(lista):
    if lista[i][0]=='a':
        lista_novo.append(lista[i])
        i+=1
    else:
        None
        i+=1
z=0
while z<len(lista_novo):
   print(lista_novo[z])
   z+=1

    

    
    
