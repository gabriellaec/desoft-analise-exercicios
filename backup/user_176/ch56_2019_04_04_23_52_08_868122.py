def calcula_total_da_nota(lista_1, lista_2):
    i=0
    s=0
    while i<len(lista_1):
        y= lista_1[i]*lista_2[i]
        i+= 1
        s+= y
    return s
