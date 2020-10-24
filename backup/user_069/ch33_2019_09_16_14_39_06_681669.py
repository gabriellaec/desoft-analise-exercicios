lista = [1]*100
soma = lista[0]
i = 0
while 99 > i:
    lista[i + 1] = lista[i]*(1/2)
    soma += lista[i + 1]
    i += 1 
print (soma)
