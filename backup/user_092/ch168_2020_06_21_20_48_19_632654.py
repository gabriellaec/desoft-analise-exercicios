def login_disponivel(x,y):
    c = 1
    i = 0
    for e in y:
        if x == e:
            while i < len(y):
                s = str(c)
                v = x+s
                if v == y[c]:
                    c +=1
                i += 1
        else:
            return x
    return v