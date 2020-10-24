def login_disponivel(txt, x):
    c = 0
    d = txt
    for i in range(len(x)):
        if d == x[i]:
            c += 1
            d = d[0:len(x)] + str(c)
    return d
            
        