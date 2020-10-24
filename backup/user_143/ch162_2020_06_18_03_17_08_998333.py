def verifica_lista (a):
    if len(a) == 0:
        return 'misturado'
    else:
        p = 0
        i = 0
        for j in a: 
            if j%2 == 0:
                p +=1
            else:
                i +=1
        if i == len(a):
            return 'ímpar'
        elif p == len(a):
            return 'par'
        else:
            return 'misturado'