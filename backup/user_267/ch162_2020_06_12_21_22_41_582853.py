def verifica_lista(l):
    im = True
    p = True
    if len(l) == 0:
        return 'misturado'
    for i in range(len(l)):
        if l[i]%2 != 0:
            p = False  
        elif l[i]%2 == 0:
            im = False
    if im and not p:
        return 'ímpar'
    elif p and not im:
        return 'par'
    else:
        return 'misturado'           
