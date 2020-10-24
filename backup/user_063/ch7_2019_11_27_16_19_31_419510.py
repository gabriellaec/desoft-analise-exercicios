def calcula_norma(lista):
    soma = 0
    x = lista[0]
    if len(lista)==2:
        y = lista[1]
        modulo = (((x)*2)+((y)2))*(1/2)
    elif len(lista)==1:
        modulo = abs(x)
    else:
        for i in lista:
            soma = soma + i**2
        modulo = soma**(1/2)
    return modulo