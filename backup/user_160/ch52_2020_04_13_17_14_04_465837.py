def calcula_total_da_nota(lista1,lista2):
    precototal = 0
    i = 0
    while i < len(lista1):
        precototal = precototal + lista1[i]*lista2[i]
        i+=1
    return (precototal)