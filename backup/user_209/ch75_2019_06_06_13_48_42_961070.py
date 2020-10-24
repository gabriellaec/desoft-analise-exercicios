def verifica_primos (listanumeros):
    dic = {}
    for numeros in listanumeros:
        primo = True
        if numeros <= 1:
            primo = False
        for e in range (2,numeros):
            if numeros % e == 0 and numero != e:
                primo = False
        dic[numeros] = primo
    return dic