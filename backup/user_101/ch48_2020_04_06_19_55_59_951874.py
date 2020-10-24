def eh_crescente(l):
    cresce = True
    i = 1
    while i < len(l):
        if l[i-1] < l[i]:
            cresce = True
            return True
        else:
            cresce = False
            return False
        i += 1