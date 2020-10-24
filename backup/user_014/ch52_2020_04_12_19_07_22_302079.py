def calcula_total_da_nota(info, preco):
    lista = []
    total = 0
    i = 0
    while len(info) == len(preco) > i:
        valor = info[i] * preco[i]
        lista.append(valor[i])
        total = total + lista[i]
        i += 1
    return total