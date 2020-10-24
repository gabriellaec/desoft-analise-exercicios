def login_disponivel(name,l):
    not_over = True
    if name in l:
        return name
    else:
        i = 1
        while not_over:
            if name+i in l :
                not_over = False
            else:
                i+1
        return name+i