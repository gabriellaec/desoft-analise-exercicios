def calcula_total_da_nota (preço, quantidade):
    nota = []
    total = 0
    i = 0
    while len(preço) == len(quantidade)>i:
        valor = preço[i]*quantidade[i]
        nota.append(valor)
        total = nota[i] + nota[i + 1]
        i = i + 1
    return total
    