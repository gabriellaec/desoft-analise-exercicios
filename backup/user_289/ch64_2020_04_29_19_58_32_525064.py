def acha_bigramas(palavra):
    lista = []
    i = 0
    while i < len(palavra) - 1:
        bigrama = palavra[i] + palavra[i+1]
        lista.append(bigrama)
        i += 1
    return lista
print(lista)