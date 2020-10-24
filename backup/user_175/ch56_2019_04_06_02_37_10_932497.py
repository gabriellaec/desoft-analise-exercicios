def calcula_total_da_nota(valor, quantidade):
    lista_final = []
   
    i = 0
    x = len(valor)
    while i < x:
        valor_final_produto = valor[i]*quantidade[i]
        lista_final.append(valor_final_produto)       
        i += 1
        
    soma = 0
    
    n = 0
    y = len(lista_final)
    while n < y:
        soma += lista_final[n]
        n += 1
        
    total = soma   
    
    return total