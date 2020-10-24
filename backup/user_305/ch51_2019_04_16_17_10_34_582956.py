
def estritamente_crescente(lista):
    lista2=[]
    if lista==[]:
        return[]
    i=0
    lista2.append(lista[0])
    while i+1<len(lista):
        if lista[i+1]>lista[i]:
            lista2.append(lista[i+1])
        i+=1
    return lista2
        
           
    