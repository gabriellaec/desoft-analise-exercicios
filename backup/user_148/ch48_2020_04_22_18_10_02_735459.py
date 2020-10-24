def eh_crescente(l):
    i = 0
    
    while i<len(l):
        if l[i+1] >= l[i]:
            return True
        else:
            return False
        i += 1
        