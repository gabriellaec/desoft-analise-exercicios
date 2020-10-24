def calcula_total_da_nota(lista1, lista2):
    x = len(lista1)
    nota = [0]*x
    cont = 0
    soma = 0
    while cont != x:
        nota[cont] = lista1[cont]*lista2[cont]
        soma = nota[cont] + soma
        cont +=1
    return soma
    