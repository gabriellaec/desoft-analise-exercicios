def verifica_progressao (n):
    
    if n == []:
        return "NA"
    
    for i in n:
        if i == 0:
            return "NA"
    r = n[1]-n[0]
    q = n [1]/n[0]
    PA = True
    PG = True
    for i in range(len(n)-1):
        if r != n[i+1]-n[i]:
            PA = False
        if q != n [i+1]/n[i]:
            PG = False
            
    if PG == True and PA == True:
        return "AG"
    if PG == True and PA == False:
        return "PG"
    if PA == True and PG == False:
        return "PA"
    else:
        return "NA"