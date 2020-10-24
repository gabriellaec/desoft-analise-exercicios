def lista_caracteres(palavra):
    i=0
    lista=[]
    while i<len(palavra):
    	if palavra[i] not in lista:
            lista.append(palavra[i])
        i+=1
	return lista