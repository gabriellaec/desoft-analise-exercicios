lista3 = []
def subtracao_de_listas(lista1,lista2):
    for i in lista1: 
    	for n in lista2:
    		if lista1[i] not in lista2[n]:
        	lista3.append(i)
    return lista3