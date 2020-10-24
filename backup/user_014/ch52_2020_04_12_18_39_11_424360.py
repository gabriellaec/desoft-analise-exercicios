def calcula_total_da_nota(info, preco):
    lista = []
    i = 0
    while len(info) == len(preco) > i:
        lista_nota = info[i] * preco[i]
        i += 1
        lista.append(lista_nota[i])
    return lista