soma = 0
i = 0   
for i in range (len(lista)):
    lista = [3,27,9,33,7,21,2,4,6,8]
    if lista[i] % 2 != 0:
        soma += lista[i]
        i += 1
print (soma)
