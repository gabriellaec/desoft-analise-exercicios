def verifica_primos (lista):
    dic = {}
    for i in lista:
        div = 0
        tam = range(2,len(lista)+1)
        for a in tam:
            if i % a == 0:
                div += 1
        if div >= 2 or i < 0 or i == 1:
            dic[i] = False
        else:
            dic[i] = True
    return dic