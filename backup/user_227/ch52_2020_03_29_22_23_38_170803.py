def calcula_total_da_nota(valor, quantidade):
    i = 0
    total_individual = []
    while i < len(valor):
        multiplicacao = valor[i]*quantidade[i]
        total_individual.append(multiplicacao)
        
        i += 1
    
    return sum(total_individual)