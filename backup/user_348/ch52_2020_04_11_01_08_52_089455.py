def calcula_total_da_nota (preço, quantidade):
    nota = []
    i = 0
    while len(preço) == len(quantidade):
        valor = preço[i]*quantidade[i]
        nota.append(valor)
        i = i + 1
        return nota
    