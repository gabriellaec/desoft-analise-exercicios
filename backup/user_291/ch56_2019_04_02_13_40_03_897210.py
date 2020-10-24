def calcula_total_da_nota(lista3, lista4):
    i = 0
    soma = 0 
    while i < len(lista4):
        soma += lista3[i]*lista4[i]
        i += 1
    return soma

    