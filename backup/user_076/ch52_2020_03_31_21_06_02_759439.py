def calcula_total_da_nota (quantidade, preço):
    contador = 0 
    soma = 0
    while contador < len(preço):
        soma += quantidade[contador] * preço[contador]
        contador += 1
    return soma