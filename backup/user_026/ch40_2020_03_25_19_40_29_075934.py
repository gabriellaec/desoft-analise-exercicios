def soma_valores(lista):
    c = 0
    soma = 0
    tamanho = len(lista)
    while c < tamanho:
        soma = soma + lista[c]
        c = c + 1
	return soma