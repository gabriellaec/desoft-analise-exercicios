def calcula_total_da_nota(itens,valor):
    soma = 0
    total = []
    while i < len(itens)-1:
        i = 0
        valor = itens[i] * valor[i]
        total.append(valor) 
        i += 1
        for numero in total:
            soma += numero
    return soma