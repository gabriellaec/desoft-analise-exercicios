def soma (lista):
    lista= []*100
    i=0
    soma= 0
    while i<len(lista):
        soma = soma + (1/2**i)
        i= i + 1
    return soma