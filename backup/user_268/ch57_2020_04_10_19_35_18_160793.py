def verifica_progressao(lista):
    a = len(lista)
    c = 0
    b = 0
    for i in range(1, (a-1)):
        while c < a:
            if (lista[i] ** 2) == lista[i - 1] * lista[i+1]:
                c+=1
                PG = True
            else:
                PG = False
                c = a    
        while b < a:
            if (lista[i] ** 2) == lista[i - 1] * lista[i+1]:
                b+=1
                PA = True
            else:
                b = a
                PA = False
            
    if PA and PG:
        return 'AG'
    elif PA:
        return 'PA'
    elif PG :
        return 'PG'
    else:
        return 'NA'