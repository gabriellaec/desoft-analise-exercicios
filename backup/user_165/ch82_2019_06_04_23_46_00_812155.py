def primeiras_ocorrencias(x):
	dicionario = {}
	for letra in x:
		if letra not in dicionario:
			dicionario[letra] = 1
		else:
			dicionario[letra]+=1
	return dicionario
x = input ("Digite uma palavra: ")
print(primeiras_ocorrencias(x))

