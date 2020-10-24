def login_disponivel(x,y):
    c = 1
    i = 0
    for e in y:
        if x == e:
            while i < len(y):
                v = x[:]+c
                if v == y[c]:
                    c +=1
                i += 1
            return v
        else:
            return x