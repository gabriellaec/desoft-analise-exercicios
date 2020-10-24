def login_disponivel(x,y):
    c = 1
    i = 0
    for e in y:
        if x == e:
            while i <= len(y):
                s = str(c)
                v = x+s
                if v == y[i]:
                    c += 1
                i += 1
            return v
    
    return x