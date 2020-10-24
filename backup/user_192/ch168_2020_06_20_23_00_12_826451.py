def login_disponivel(txt, x):
    c = 0
    d = 0
    for i in range(len(x)):
        if txt == x[i]:
            c += 1
            d = txt[0:len(txt)] + str(c)
    return d
            
        