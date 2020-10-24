def verifica_progressao(lista):
    q = lista[1]/lista[0]
    r = lista[1] - lista[0]      
    qn = lista[2]/lista[1]
    rn = lista[2] - lista[1] 
    continua = True
    continua2 = True
    if qn == q:
        while continua == True:
            while i < len(lista):    
                qn = lista[i+1]/lista[i]
                if qn != q:
                    continua = False
                    break
                else:
                    i += 1
                    break
            return "PG"
    if rn == r:  
        while continua2 == True:
            for i < len(lista):
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