def inverte_dicionario(dicionario):
    inversão = {}
    for e in dicionario:
        valor = dicionario[e]
        inversão[valor] = e
    
	return inversão    
