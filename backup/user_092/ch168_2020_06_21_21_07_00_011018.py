def login_disponivel(x,y):
    c = 1
    for e in y:
        if x == e:
            for i in y:
                s = str(c)
                v = x+s
                if v == i:
                    c += 1
            return v
    
    return x