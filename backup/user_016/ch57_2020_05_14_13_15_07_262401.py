def verifica_progressao(lista0):
    u = 0
    n = -1
    h = 0
    b = 1
    if len(lista0)%2 == 0:
        lista1 = []
        lista2 = []
        while u < len(lista0)/2:
            a = (lista0[u] + lista0[n])/2
            lista1.append(a)
            u += 1
            n -= 1
        while b < len(lista0):
            if lista0[b] == 0 or lista0[h] == 0:
                PG = False
                break
            else:
                p = lista0[b]/lista0[h]
                lista2.append(p)
            b += 1
            h += 1
        exercicio1 = True
        exercicio2 = True
        d = 0
        f = 0
        while exercicio1:
            if lista1[f] == a:
                if f == len(lista1)-1:
                    PA = True
                    break
                else:
                    pass
            else:
                PA = False
                break
            f += 1
        while exercicio2:
            if b == 0 or h == 0:
                PG = False
                break
            if lista2[d] == p:
                if d == len(lista2) - 1:
                    PG = True
                    break
                else:
                    pass
            else:
                PG = False
                break
            d += 1
    else:
        lista1 = []
        lista2 = []
        while u < (len(lista0)-1)/2:
            a = (lista0[u] + lista0[n])/2
            lista1.append(a)
            u += 1
            n -= 1
        while b < len(lista0):
            if lista0[b] == 0 or lista0[h] == 0:
                break
            else:
                p = lista0[b]/lista0[h]
                lista2.append(p)
                b += 1
                h += 1
        exercicio1 = True
        exercicio2 = True
        d = 0
        f = 0
        q = int((len(lista0)-1)/2)
        j = lista0[q]
        while exercicio1:
            if lista1[f] == a and j == a :
                if f == len(lista1)-1:
                    PA = True
                    break
                else:
                    pass
            else:
                PA = False
                break
            f += 1
        while exercicio2:
            if b == 0 or h == 0:
                PG = False
                break
            if lista2[d] == p:
                if d == len(lista2) - 1:
                    PG = True
                    break
                else:
                    pass
            else:
                PG = False
                break
            d += 1
    if PA == True and PG == True:
        return 'AG'
    elif PA == True:
        return 'PA'
    elif PG == True:
        return 'PG'
    else:
        return 'NA'