def eh_crescente(l):
    i = 0
    while i<len(l):
        if len(l)>1:
            if l[i+1] - l[i] > 0:
                return True
            else:
                return False
            i += 1
        else:
            return False    
        