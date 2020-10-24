def monta_mala(lista):
	S = 0
	lista_retorno = []
	for i in lista:
		while S < 23:
			lista_retorno.append(lista[i])
			S += lista[i]
	return lista_retorno
  
