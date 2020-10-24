def verifica_primos (listanumeros):
    dic = {}
    for numeros in listanumeros:
        eh_primo = True
        if numeros <= 1:
            eh_primo = False
        for e in range (2,numeros):
            if numeros % e == 0 and numero != e:
                eh_primo = False
        dic[numeros] = eh_primo
    return dic