def calcula_total_da_nota (preço, quantidade):
    nota = []
    total = 0
    i = 0
    while len(preço) == len(quantidade)>i:
        valor = preço[i]*quantidade[i]
        nota.append(valor)
        total = total + nota[i]
        i = i + 1
    return total
    