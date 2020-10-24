def login_disponivel(a, l):
    i = 1
    for a in l:
        while "{0}{1}".format(a, i):
            i += 1
            
        return "{0}{1}".format(a, i)
    if a not in l:
        return a
            