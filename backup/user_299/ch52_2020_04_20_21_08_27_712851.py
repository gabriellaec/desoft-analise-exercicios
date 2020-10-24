def calcula_total_da_nota(listap,listaq):
    gastopproduto = []
    for i,e in listap:
        gastopproduto.append(e*listaq[i])
    soma = 0
    for valor in gastopproduto:
        soma = soma + valor
    
    return soma