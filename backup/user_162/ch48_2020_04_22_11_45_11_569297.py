def eh_crescente(l):
    crescente  = True
    i = 1
    while i < len(l):
        if l[i-1] >= l[i]:
            crescente = False
        i+=1
    if crescente:
        return True 
    else:
        return False