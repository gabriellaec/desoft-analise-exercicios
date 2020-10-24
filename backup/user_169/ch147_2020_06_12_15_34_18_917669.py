
def mais_frequente(lista):
    lista2=[]
    for i in lista:
        lista2.append(lista.count(i))

    for e in lista:
        if lista.count(e)<max(lista2):
            lista.remove(e)

    return lista[-1]
            
    

