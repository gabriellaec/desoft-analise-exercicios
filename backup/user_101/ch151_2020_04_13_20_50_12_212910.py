def eh_crescente(l):
    cresce = True
    i = 1
    while i < len(l):
        if l[i-1] < l[i] and cresce == True:
            cresce =  True
        else:
            cresce = False
        i += 1
    if cresce == True:
        return True
    else:
        return False

def eh_decrescente(l):
    decresce = True
    i = 1
    while i < len(l):
        if l[i-1] > l[i] and decresce == True:
            decresce =  True
        else:
            decresce = False
        i += 1
    if decresce == True:
        return True
    else:
        return False

def classifica_lista(l):
    c = 'crescente'
    d = 'descrescente'
    n = 'nenhum'
    if len(l) == 0:
        return n
    else:
        if eh_crescente(l) == True:
            return c
        elif eh_decrescente(l) == True:
            return d
        else:
            return n

