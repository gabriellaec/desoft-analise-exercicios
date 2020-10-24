def verifica_primos(numeros):
    dicionario = {}
    for e in numeros:
        if e < 2 or (e % 2 == 0 and e > 2):          
            dicionario[e] = False
        elif e == 2 or e == 3:
            dicionario[e] = True
        else:
            intervalo = range(1, e, 2)
            for i in intervalo:
                a = e % i
            if a == 0:
                dicionario[e] = False
            else:
                dicionario[e] = True        
    return dicionario