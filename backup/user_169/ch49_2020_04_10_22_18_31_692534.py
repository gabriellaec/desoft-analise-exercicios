exemplo=[1,2,3,4,5]
def inverte_lista(lista):
    i=0
    lista2=[]
    while i<len(lista):
        lista2.append(lista[0-i])
        i+=1
       
    
    return lista2