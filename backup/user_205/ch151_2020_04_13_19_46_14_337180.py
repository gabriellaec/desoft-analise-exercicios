
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
    
def estritamente_decrescente(lista):
    if lista == []:
        return lista
    else:
        inicio = lista[0]
        cresce=[inicio] 
        for i in range(len(lista)-1):
            if lista[i+1]<inicio:
                inicio = lista[i+1]
                cresce.append(lista[i+1])
        return decresce
def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    elif estritamente_crescente(lista):
        return "crescente"
    elif estritamente_decrescente(lista):
        return "descrescente"
    else:
        return "nenhum"