def login_disponivel(txt, x):
    c = 0
    d = txt
    for i in range(len(x)):
        if txt == x[i]:
            c += 1
            d = txt[0:len(x)] + str(c)
    return d
            
        