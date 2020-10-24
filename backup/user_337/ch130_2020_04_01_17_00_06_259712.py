def monta_mala(lista):
    i = 0
    lista_nova = [lista[i]]
    soma = 0
    while i < len(lista):
        soma = soma + lista [i]
        if soma <= 23:
            lista_nova.append(lista[i+1])
        else:
            break
    return (lista_nova)