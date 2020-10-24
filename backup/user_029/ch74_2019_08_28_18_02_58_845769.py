def conta_bigramas(palavra):
    listab = []
    i = 1
    while i != len(palavra):
        if palavra[i-1] + palavra[i] not in listab:
            listab.append(palavra[i-1]+palavra[i])
        
    
        i += 1
    
    return listab