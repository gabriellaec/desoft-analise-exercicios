
def estritamente_crescente(lista):
    lista2=[]
    if lista==[]:
        return[]
    i=0
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista2.append(lista[i])
        i+=1
    return lista2
        
           
    