def calcula_norma(lista):
    #|v| = (a**2 + b**2 + ... + n**2)**1/2
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    a = sum(lista2)
    v = a **1/2
    return v