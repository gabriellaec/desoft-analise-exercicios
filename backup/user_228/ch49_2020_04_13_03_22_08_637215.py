def inverte_lista(lista):
    a=1
    lista2=[]
    for i in range(len(lista)):
        lista2.append(lista[(len(lista)-a)])
        a+=1
    return lista2

                      
        
        