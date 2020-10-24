def verifica_primos(numeros):
    dic = dict()
    for i in range(len(numeros)-1):
        if numeros[i] <= 1:
            dic[numeros[i]] = False
        elif numeros[i] == 2:
            dic[numeros[i]] = True
        elif numeros[i]%2 == 0:
            dic[numeros[i]] = False
        else:
            x = 3
            while x < numeros[i]-2:
                if (numeros[i])%x != 0:
                    x += 2
                else:
                    dic[numeros[i]] = False
            dic[numeros[i]] = True
    return dic