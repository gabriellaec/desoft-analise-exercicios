def lista_caracteres(x):
    lista = []
    
    for i in x:
        lista.append(i)
    j = 1
    
    for k in lista:
        while j < len(lista):
            if k == lista[j]:
                del(lista[j])
            j+=1
	return lista