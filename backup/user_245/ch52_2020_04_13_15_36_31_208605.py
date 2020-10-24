def calcula_total_da_nota(precos,quant):
    soma = 0 
    cont = 0
    while cont < len(precos):
        soma += precos[cont]*quant[cont]
        cont+=1
    return soma