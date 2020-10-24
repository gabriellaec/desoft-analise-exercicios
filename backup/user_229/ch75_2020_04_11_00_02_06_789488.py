def verifica_primos(numeros):
    dic = dict()
    for i in range(0,len(numeros)-1):
        if numeros[i] == 0 or numeros[i] == 1:
            dic[numeros[i]] = 'não'
        elif numeros[i] == 2:
            dic[numeros[i]] = 'primo'
        elif numeros[i]%2 == 0:
            dic[numeros[i]] = 'não'
        else:
            x = 3
            while x < numeros[i]:
                if (numeros[i])%x != 0:
                    x += 2
                else:
                    dic[numeros[i]] = 'não'
            dic[numeros[i]] = 'primo'
    return dic
print(verifica_primos([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))