i = 1
lista=[0]
contador = 0
y = True
while y:
 
    if(lista[contador]==1):
        y=False
        print(lista)

    elif(lista[contador]== 0):
        b = lista[contador]*3+1
        lista.append(b)
        contador +=1
    
    if(lista[contador]%2 == 0):
        b = lista[contador]/2
        lista.append(b)
        contador +=1
    else:
        b = lista[contador]*3+1
        contador +=1
        lista.append(b)
