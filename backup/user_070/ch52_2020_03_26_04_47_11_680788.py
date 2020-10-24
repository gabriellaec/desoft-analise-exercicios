def calcula_total_da_nota(preco, qnt):
    soma = 0
    parcela = 0
    n = len(qnt)
    i = 0
    while i < n:
        parcela = preco[i] * qnt[i]
        soma += parcela
        i += 1
    return soma