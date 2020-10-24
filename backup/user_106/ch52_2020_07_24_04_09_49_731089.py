def calcula_total_da_nota(precos, quantidades):
    valor = 0
    for i in range(0, len(precos)):
        valor += precos[i] * quantidades[i]
    return valor