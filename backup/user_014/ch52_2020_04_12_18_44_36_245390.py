def calcula_total_da_nota(info, preco, lista_nota):
    lista = []
    i = 0
    while len(info) == len(preco) > i:
        valor = info[i] * preco[i]
        lista.append(valor)
        i += 1
    return lista