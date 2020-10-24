def calcula_total_da_nota (quantidade, preço):
    contador = 0 
    valor = []
    soma = 0
    while contador < len(quantidade):
        valor[contador] = quantidade[contador] * preço[contador]
        soma += valor[contador]
        contador += 1
    return soma