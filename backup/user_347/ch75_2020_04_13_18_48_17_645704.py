def verifica_primos(numeros):
    dicionario={}
    for n in numeros:
        if n == -1 or n==0 or n ==1:
            dicionario[n] = False
        elif n==2:
            dicionario[n] = True
        else:
            dicionario[n] = True
            if n%2==0:
                dicionario[n] = False
            else:
                d = 3
                while n > d:
                    if n%3==0:
                        dicionario[n] = False
                        break
                    else:
                        d+=2
    return dicionario