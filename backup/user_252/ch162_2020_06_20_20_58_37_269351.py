def verifica_lista(num):
    if len(num)==0:
        return 'misturado'
    par=True
    impar=True
    i=0
    while i < len(num):
        if num[i]%2==0:
            impar=False
        if num[i]%2!=0:
            par=False
        i+=1
    if par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'