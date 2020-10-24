def monta_mala(lista):
	S = 0
	lista_retorno = []
	while S < 23:
		for i in lista:
			lista_retorno.append(lista[i])
			S += lista[i]
	return lista_retorno
  
