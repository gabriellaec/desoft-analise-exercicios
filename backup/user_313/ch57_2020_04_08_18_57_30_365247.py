def verifica_progressao (l1):
    if len(l1) < 2:
        return "NA"
    
    if len(l1) == 2:
        return "AG"

    if l1[0] == 0 and l1[1] == 0:
        return "NA"

    razãoPa = l1[1]-l1[0]
    razãoPg = l1[1]/l1[0]

    PA = True
    PG = True

    while True:
        for i in range(0,len(l1)-1):
            if l1[i+1]-l1[i] != razãoPa:
                PA = False
                break
        break

    while True:
        if l1[i] != 0:
            PG = False
            break
        for i in range(0,len(l1)-1):
            if l1[i+1]/l1[i] != razãoPg:
                PG = False 
                
                break
        
        break

    if PA and PG:
        return "AG"

    elif PA:
        return "PA"

    elif PG:
        return "PG"

    else:
        return "NA"