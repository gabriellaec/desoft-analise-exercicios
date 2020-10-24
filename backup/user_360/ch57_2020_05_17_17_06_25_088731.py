def verifica_progressao(num):
    if num == []:
        return 'NA'
    if len(num) < 3:
        return 'NA'
    
    for i in num:
        if i == 0:
            return 'NA'
    x = num[1] - num[0]
    y = num[1] / num[0]
    PA = True 
    PG = True 
    for i in range(len(num)-1):
        if y != num[i+1] / num[i]:
            PG = False
        if x != num[i+1] - num[i]:
            PA = False
        
    if PG == True and PA == True:
        return 'AG'
    if PG == True and PA == False:
        return 'PG'
    if PG == True and PA == True:
        return 'PA'
    else:
        return 'NA'