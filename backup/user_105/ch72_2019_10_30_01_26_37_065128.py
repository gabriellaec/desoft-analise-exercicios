def lista_caracteres(x):
    lista = []
    for i in x:
        lista.append(i)
    while z<len(lista):
        for j in lista:
            if j == lista[i]:
                del(lista[i])
        z+=1
    return lista
            
        
        
    