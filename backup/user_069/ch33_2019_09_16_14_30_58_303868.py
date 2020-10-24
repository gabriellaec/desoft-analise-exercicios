def soma_elementos ():
    lista = [1]
    soma = 0
    i = 0
    while i < 99:
        lista[i + 1] = lista[i]*(1/2)
        soma += lista[i + 1]
    	i += 1
print (soma_elementos())