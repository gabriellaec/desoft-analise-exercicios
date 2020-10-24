def verifica_progressao(lista):
    r = lista[1] - lista[0]
    rn = lista[2] - lista[1] 
    PA = False
    PG = False
    if rn == r:
        for i in range(2,len(lista)+2):
            rn = (lista[i]) - (lista[i-1])
            if rn != r:
                PA == False
                break
            else:
                i += 1
            PA = True
    
    if lista[0] != 0 and lista[1] != 0:
        q = lista[1]/lista[0]
        qn = lista[2]/lista[1]
        if qn == q:
            for i in range(2,len(lista)+2):
                if lista[i] != 0:
                    qn = (lista[i])/(lista[i-1])
                    if qn != q:
                        PG == False
                        break
                    else:
                         i += 1
                
                else:
                    PG == False
                    break
                PG = True

    if PA and PG:
        return "AG"
    elif PA:
        return "PA"
    elif PG:
        return "PG"
    else:
        return "NA"