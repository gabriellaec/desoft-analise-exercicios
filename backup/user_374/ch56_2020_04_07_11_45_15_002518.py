def calcula_norma(lista):
    soma = 0
    norm = []
    cont = 0
    for i in lista:
        norm.append(i**2)
        soma += norm[cont]
        cont += 1
    raiz = soma**(1/2)
    return raiz
