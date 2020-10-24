def calcula_total_da_nota(lista1, lista2):
    s = 0
    i = 0
    result = 0
    while i<= len(lista1)-1:
        s= lista1[i]*lista2[i]
        i+=1
        result +=s
    return result