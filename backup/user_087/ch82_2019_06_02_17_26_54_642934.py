def primeiras_ocorrencias(palavra):
    letra_indice = dict()
    for letra in palavra:
		i = 0
        while i < len(palavra):
        	if letra in letra_indice:
           		letra_indice[letra] = palavra[i]
            	i += 1
	return letra_indice