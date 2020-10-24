def verifica_primos(numeros):
    dic = dict()
    for i in range(len(numeros)):
        if numeros[i] <= 1:
            dic[numeros[i]] = False
        elif numeros[i] == 2 or numeros[i] == 3 or numeros[i] == 5:
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
                    break
                dic[numeros[i]] = True
    print(dic)