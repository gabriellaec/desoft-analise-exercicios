def soma_elementos ():
    lista = [1]*100
    soma = 1
    i = 0
    while i < 99:
        lista[i + 1] = lista[i]*(1/2)
        soma += lista[i + 1]
        i += 1
    return soma
print (soma_elementos())