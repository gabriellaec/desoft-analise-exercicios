def verifica_progressao(l):
    r = l[1]/l[0]
    d = l[1] - l[0]
    vpa, vpg = True, True
    
    if len(l) == 0:
        return 'NA'
    
    for i in range(len(l)-1):
        print(l[i], i)
        if l[i+1]/l[i] != r:
            vpg = False
        if l[i+1] - l[i] != d:
            vpa = False

    if vpg == True and vpa == True:
        return 'AG'
    elif vpg == True:
        return 'PG'
    elif vpa == True:
        return 'PA'
    else:
        return 'NA'
