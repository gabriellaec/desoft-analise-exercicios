def calcula_total_da_nota(precos, produtos):
    nota = dict()
    for i in range(len(produtos)):
        nota[produtos[i]] = precos[i]
    soma = sum(nota.values())
    return soma