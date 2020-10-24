def verifica_progressao(l):
    r = l[1]/l[0]
    d = l[1] - l[0]
    vpa, vpg = True, True
    
    for i in range(len(l)-1):
        print(l[i])
        if l[i+1]/l[i] != r:
            vpg = False
        if l[i+1] - l[i] != d:
            vpa = False
    if vpg == vpa:
        return 'AG'
    elif vpg == True:
        return 'PG'
    elif vpa == True:
        return 'PA'
    else:
        return 'NA'

