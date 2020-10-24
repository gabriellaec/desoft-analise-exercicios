def inverte_lista(lista):
    a=1
    lista2=[]
    for i in lista:
        lista2.append(lista[(len(lista)-a)])
        i+=1
        a+=1
    return lista2

                      
        
        