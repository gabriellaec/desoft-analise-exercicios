def verifica_primos(L):
    dicionario = {}
    i = 0
    while i < len(L):
        divisor = 2
        primo = True
        L[i] = int(lista[i])
        if L[i] < 2:
            dicionario[L[i]] = False
        elif L[i] == 2:
            dicionario[L[i]] = True
        else:
            while divisor < L[i]:
                if L[i] % divisor == 0:
                    primo = False
                divisor += 1
            dicionario[L[i]] = primo
            i += 1
        return dicionario