def verifica_progressao(lista):
    if len(lista) < 3:
        return "NA"
    
    test = 0
    isPA = True
    
    for i in range(1, len(lista) -1):
       if i == 1:
            test = lista[i] - lista[i-1]
        else:
            if lista[i] - lista[i-1] != test:
                isPA = False
                break
                
   	isPG = True
    
    for i in range(1, len(lista) -1):
        if lista[i-1] == 0:
            isPG = False
            break
        if i == 1:
            test = lista[i] / lista[i-1]
        else:
            if lista[i] / lista[i-1] != test:
                isPG = False
                break
    
    if isPA and isPG:
        return "AG"
    elif isPA:
        return "PA"
    elif isPG:
        return "PG"
    else:
        return "NA"