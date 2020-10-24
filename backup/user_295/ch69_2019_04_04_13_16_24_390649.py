def junta_listas (lista):
    lista_simples=[]
    i = 0
    while i < len(lista):
        r = 0
        while r < len (lista[i]):
            lista_simples.append((lista[i])[r])
            r += 1
        i += 1  
    return lista_simples