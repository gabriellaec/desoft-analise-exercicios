
def estritamente_crescente(lista):
    lista2=[]
    if lista==[]:
        return lista
    i=1
    s=0
    lista2.append(lista[0])
    while i<len(lista):
        if lista[i]>lista2[s]:
            s+=1
            lista2.append(lista[i+1])
            
        i+=1
    return lista2
        
           
    