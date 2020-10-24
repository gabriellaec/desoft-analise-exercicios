def verifica_lista(l):
    if len(l) == 0:
        return 'misturado'
    else:
        for i in range(len(l)-1)::
            if l[i]%2 != 0:
                return 'ímpar'
            elif l[i]%2 == 0:
                return 'par'
            else:
                return 'misturado'           
