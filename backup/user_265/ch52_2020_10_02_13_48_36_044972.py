def calcula_total_da_nota(itens,valor):
    i = 0
    total = []
    while i < len(itens):
        valor = itens[i] * valor[i]
        total.append(valor) 
        i += 1
    return total

def soma(total):
    soma = 0
    for numero in total:
        soma += numero
        return soma