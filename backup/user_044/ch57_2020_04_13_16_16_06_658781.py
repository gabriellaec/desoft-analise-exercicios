def verifica_progressao(ls):
    if (ls[1]-ls[0])==(ls[2]-ls[1]):
        return 'PA'
    elif ((ls[2]-ls[1])/(ls[1]-ls[0]))==((ls[3]-ls[2])/(ls[2]-ls[1])):
        return 'PG'
    else:
        return 'NA'