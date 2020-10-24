def login_disponivel(txt, x):
    c = 0
    for i in range(len(x)):
        if txt == x[i]:
            c += 1
            d = txt[0:len(x)] + str(c)
    return d
            
        