def verifica_lista(l):
    if len(l) == 0:
        return 'misturado'
    else:
        for i in l:
            if i%2 != 0:
                return 'ímpar'
            elif i%2 == 0:
                return 'par'
            else:
                return 'misturado'           
   