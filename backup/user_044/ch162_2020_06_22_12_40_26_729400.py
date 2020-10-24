def verifica_lista(ls):
    par = 0
    impar = 0
    for i in ls:
        if i%2==0:
            par+=1
        elif i%2==1:
            impar+=1
    if ls == []:
        return 'misturado'
    elif par == len(ls):
        return 'par'
    elif impar == len(ls):
        return 'ímpar'
    else:
        return 'misturado'
        