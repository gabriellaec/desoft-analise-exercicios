def calcula_total_da_nota(precos, quantidade):
    nota = list()
    for i in range(len(precos)):
        nota.append(precos[i]*quantidade[i])
    return sum(nota)