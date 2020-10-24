def calcula_total_da_nota(info, preco):
    lista = []
    total = 0
    i = 0
    while i < len(info) == len(preco):
        valor = info[i] * preco[i]
        lista.append(valor)
        total = total + lista[i]
        i += 1
    return total