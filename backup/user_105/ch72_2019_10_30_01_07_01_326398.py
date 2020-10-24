def lista_caracteres(x):
    lista = []
    for i in x:
        lista.append(i)
    while i<len(lista):
        for j in lista:
            if j == lista[i]:
                del(lista[i])
        i+=1
    return lista
            
        
        
    