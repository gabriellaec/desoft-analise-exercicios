def numero_no_indice (lista):
    i = 0
    listaNova = []
    while (i < len(lista)):
        if(i == lista[i]):
            numero = i
            listaNova.append(numero)
        i += 1
    return (listaNova)

lista = [0,2,2,3,6]

print(numero_no_indice(lista))