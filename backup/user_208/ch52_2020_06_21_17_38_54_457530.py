def calcula_total_da_nota (item, preco):
    i = 0
    soma = 0
    while i < len(item):
        x = item[i]*preco[i]
        soma = soma + x
        i+=1
    return soma    
        