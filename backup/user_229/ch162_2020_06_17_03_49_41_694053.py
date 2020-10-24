def verifica_lista(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
     
    if len(pares) > 0:
        if len(impares) > 0:
            return 'misturado'
        else:
            return 'par'
    elif len(impares) > 0:
        return 'impar'
    else:
        return 'misturado'