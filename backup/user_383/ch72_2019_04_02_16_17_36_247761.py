def lista_caracteres(palavra):
	cont=0
    lista_vazia=[]
    while cont<len(palavra):
        if palavra[cont] not in lista_vazia:
            lista_vazia.append(palavra[cont])
        cont+=1
    return lista_vazia
