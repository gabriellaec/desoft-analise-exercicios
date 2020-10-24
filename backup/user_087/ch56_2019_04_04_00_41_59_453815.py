def calcula_total_da_nota(preço, qtd):
    soma = 0
    i = 0
    while i < len(preço):
        soma = soma + (preço[i]*qtd[i])
        i += 1
    return soma 