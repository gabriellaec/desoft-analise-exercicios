def verifica_progressao(lista):
    r = lista[1] - lista[0]
    rn = lista[2] - lista[1] 
    continua = True
    continua2 = True
    i = 0
    if lista[0] != 0 and lista[1] != 0:
        q = lista[1]/lista[0]
        qn = lista[2]/lista[1]
        if qn == q:
            while continua == True:
                while i <= len(lista):
                    if lista[i] != 0:
                        qn = lista[i+1]/lista[i]
                        if qn != q:
                            continua = False
                            break
                        else:
                            i += 1
                            break
                    else:
                        continua = False
                        break
                return "PG"
        i = 0
        if rn == r:  
            while continua2 == True:
                while i <= len(lista):
                    rn = lista[i+1] - lista[i]
                    if rn != r:
                        continua = False
                        break
                    else:
                        i += 1
                        break
                return "PA"
        else:
            return "NA"
    else:
        if rn == r:  
            while continua2 == True:
                while i < len(lista):
                    rn = lista[i+1] - lista[i]
                    if rn != r:
                        continua = False
                        break
                    else:
                        i += 1
                        break
                return "PA"
        else:
            return "NA"