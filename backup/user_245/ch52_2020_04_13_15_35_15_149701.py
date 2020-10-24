def calcula_total_da_nota(precos,quantidade):
    cont = 0
    soma = 0
    for i in precos:
        soma += precos[i]*quantidade[i]
    return soma