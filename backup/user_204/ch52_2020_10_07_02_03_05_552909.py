def calcula_total_da_nota(info,valor):
    i = 0
    final = []
    while i < len(info):
        final[i] = info[i] * valor[i]
        i += 1 
    return final
    