
def estritamente_crescente(lista):
    if lista == []:
        return lista
    else:
        inicio = lista[0]
        cresce=[]
        cresce[0]=inicio 
        for i in range(len(lista)-1):
            if lista[i+1]>inicio:
                cresce.append(lista[i+1])
        return cresce
                
        
    

    return c