n = [ 1, 2, 3, 4 ]
n_elementos = len(n)

def soma_valores(soma):
    i = 0
    soma = 0
    while i < n_elementos:
        soma += n[i]
    i += 1
	return soma
    