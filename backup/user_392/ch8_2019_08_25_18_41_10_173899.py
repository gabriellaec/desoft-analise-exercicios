def verifica_progressao(x):
    i=0
    PA = True
    PG = True
    if len(x)>=3:
        while i<len(x)-2:
            if not 2*x[i+1] == x[i]+x[i+2]:
                PA = False
            if not (x[i+1])**2 == (x[i])*(x[i+2]):
                PG = False
                print((x[i+1])**2)
                print((x[i])*(x[1+2]))
                print(i)
            i +=1
        if PG == True and PA == True:
            return 'AG'
        elif PG == True and PA == False:
            return 'PG'
        elif PG == False and PA == True:
            return 'PA'
        else:
            return'NA'
    else:
        return 'NA'