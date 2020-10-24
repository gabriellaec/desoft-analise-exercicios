def mais_frequente(lista):
    lista3=[]
    for i in range(len(lista)):
        lista.count(lista[i]) 
        lista3.append(lista.count(lista[i]))
    for i in lista:
        if lista.count(i)<max(lista3):
            lista.remove(i)
    

    for e in range(len(lista)):
        return lista[e]