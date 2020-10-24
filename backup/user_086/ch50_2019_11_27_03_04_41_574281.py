def numero_no_indice(lista):
    lista_iguais = []
    for i in range(len(lista)):
    	if lista[i] == i:
        	lista_iguais.append(lista[i])
    return lista_iguais