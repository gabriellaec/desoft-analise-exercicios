def calcula_total_da_nota(lista1, lista2):
    i=0
    total=0
    while i < len(lista1) and len(lista2):
        total += lista1[i]*lista2[i]
    return total