def login_disponivel(name,l):
    not_over = True
    if name not in l:
        return name
    else:
        i = 1
        while not_over:
            if name+str(i) not in l :
                not_over = False
            else:
                i+=1
        return name+str(i)