def numero_no_indice(l):
    l1 = []
    x = 0
    while x<len(l):
        if l[x]==x:
            l1.append(x)    
        else:
            pass
        x+=1
    return l1