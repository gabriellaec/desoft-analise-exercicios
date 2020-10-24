def calcula_total_da_nota(lista1, lista2):
    soma = 0
    i = 0
    resultado = 0
    while i <= len(lista1)-1:
        soma = lista1[i]*lista2[i]
        i += 1
        resultado += soma
    return resultado