def verifica_progressao(lista):
    if len(lista) < 3:
        return "NA"
    
    teste = 0
    is_PA = True
    
    for i in range(1, len(lista)):
        if i == 1:
            teste = lista[i] - lista[i-1]
            print(teste)
        else:
            print(lista[i] - lista[i-1])
            if lista[i] - lista[i-1] != teste:
                is_PA = False
                break
    is_PG = True
    
    for i in range(1, len(lista)):
        if lista[i-1] == 0:
            is_PG = False
            break
        if i == 1:
            teste = lista[i]/lista[i-1]
        else:
            if lista[i]/lista[i-1] != teste:
                is_PG = False
                break
              
    if is_PA and is_PG:
        return "AG"
    elif is_PA:
        return "PA"
    elif is_PG:
        return "PG"
    else:
        return "NA"