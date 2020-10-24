def calcula_total_da_nota(info, preco):
    lista_nota = []
    i = 0
    while info == preco:
        info[i] = preco[i]
        i += 1
    lista_nota.append([info[i], preco[i]])