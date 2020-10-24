def calcula_total_da_nota(itens,valor):
    soma = 0
    total = []
    i = 0
    while i < len(itens):
        s = itens[i] * valor[i]
        total.append(s) 
        i += 1
    for numero in total:
        soma += numero
    return soma