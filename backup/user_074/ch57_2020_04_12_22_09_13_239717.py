def verifica_progressao(l):
    print(l)
    if l[1]-l[0]==l[2]-l[1]:
        return 'PA'
    if l[0]/l[1]==l[2]/l[1]:
        return 'PG'
    if l[1]- l[0]==l[2]- l[1] and l[1]/l[0]==l[2]/l[1]:
        return 'AG'
    else:
        return 'NA'
    
    