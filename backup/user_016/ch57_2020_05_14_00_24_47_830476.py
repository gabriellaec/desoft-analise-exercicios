def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        for i  in range(0,len(lista)-1):
            if lista[i+1] > lista[i]:
                pass
            else:
                break
            if i == len(lista)-2:
                return 'crescente'
        for u in range(0,len(lista)-1):
            if lista[u+1] < lista[u]:
                pass
            else:
                break
            if u == len(lista)-2:
                return 'decrescente'
    return 'nenhum'
def verifica_progressao(lista0):
    PA = True
    PG = True
    if classifica_lista(lista0) == 'nenhum':
        return 'NA'
    else:
        u = 0
        n = -1
        h = 0
        b = 1
        if len(lista0)%2 == 0:
            lista1 = []
            lista2 = []
            while u <= len(lista0)/2:
                a = (lista0[u] + lista0[n])/2
                lista1.append(a)
                u += 1
                n -= 1
            while b < len(lista0):
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
                if lista1[f] == a and j-(j-1) == a and (j+1)-j ==a:
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
                
                
            