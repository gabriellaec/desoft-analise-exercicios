def calcula_total_da_nota(preco, quantidade):
    for p, q in preco, quantidade:
        soma += (p * q)
    return soma