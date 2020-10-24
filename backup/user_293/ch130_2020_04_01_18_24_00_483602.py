def monta_mala(lista):
    lista_nova = []
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        if soma <= 23:
            lista_nova.append(lista[i])
        i += 1
    return lista_nova