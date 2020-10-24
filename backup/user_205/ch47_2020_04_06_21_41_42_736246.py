
def estritamente_crescente(lista):
    if lista == []:
        return lista
    else:
        inicio = lista[0]
        cresce=[inicio] 
        for i in range(len(lista)-1):
            if lista[i+1]>inicio:
                inicio = lista[i+1]
                cresce.append(lista[i+1])
        return cresce
                
       