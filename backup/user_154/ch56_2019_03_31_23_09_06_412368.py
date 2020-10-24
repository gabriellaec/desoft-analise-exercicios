def calcula_total_da_nota(preços, quantidade):
    soma = 0
    
    i = 0
    
    while i < len(preços):
        soma = soma + preços[i]*quantidade[i]
        i = i + 1
    return soma