def soma_impares(lista):
    l = []
    soma = 0
    a = len(lista)
    x = 0
    while x<a:
        if lista[x] % 2 != 0:
            l.append(lista[x])
            x+=1
        else:
            x+=1
    soma = sum(l)
    return soma 