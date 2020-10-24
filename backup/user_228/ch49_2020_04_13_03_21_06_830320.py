def inverte_lista(lista):
    i=0
    a=1
    lista2=[]
    while i<len(lista):
        lista2.append(lista[(len(lista)-a)])
        i+=i
        a+=1
    return lista2

                      
        
        