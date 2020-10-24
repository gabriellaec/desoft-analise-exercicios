def calcula_total_da_nota(itens,valor):
    i = 0
    soma = 0
    total = []
    while i < len(itens)-1:
        valor = itens[i] * valor[i]
        total.append(valor) 
        i += 1
        for numero in total:
        soma += numero
    return soma