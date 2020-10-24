def login_disponivel(txt, x):
    for i in range(len(x)):
        if txt not in x:
            return txt
        else:
            txt[-1] = 