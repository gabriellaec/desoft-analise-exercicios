def verifica_primos(numeros):
    dic = dict()
    for i in range(0,len(numeros)):
        if numeros[i] <= 1:
            dic[numeros[i]] = False
        elif numeros[i] == 2:
            dic[numeros[i]] = True
        elif numeros[i]%2 == 0:
            dic[numeros[i]] = False
        else:
            x = 3
            while x < numeros[i]:
                if (numeros[i])%x != 0:
                    x += 2
                else:
                    dic[numeros[i]] = False
            dic[numeros[i]] = True
    return dic
print(verifica_primos([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))