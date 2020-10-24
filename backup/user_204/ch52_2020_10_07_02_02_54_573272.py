def calcula_total_da_nota(info,valor):
    i = 0
    while i < len(info):
        final = []
        final[i] = info[i] * valor[i]
        i += 1 
    return final
    