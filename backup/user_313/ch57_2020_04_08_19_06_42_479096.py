def verifica_progressao (l1):
    PA = True
    PG = True

    if len(l1) < 2:
        return "NA"
    
    elif len(l1) == 2:
        return "AG"

    elif l1[0] == 0 and l1[1] == 0:
        PG = False
    
    elif l1[0] == 0 or l1[1] == 0:
        PG = False

    

    if PA:
        razãoPa = l1[1]-l1[0]

    if PG:
        razãoPg = l1[1]/l1[0]
    

    while PA:
        for i in range(0,len(l1)-1):
            if l1[i+1]-l1[i] != razãoPa:
                PA = False
                break
        break

    while PG:
        
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