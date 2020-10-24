def login_disponivel(l):
    not_over = True
    name = l[1]
    if l[1] in l[2]:
        name = l[1]
        return name
    else:
        i = 1
        while not_over:
            if name+i in l[2] :
                not_over = False
            else:
                i+1
        return name+i