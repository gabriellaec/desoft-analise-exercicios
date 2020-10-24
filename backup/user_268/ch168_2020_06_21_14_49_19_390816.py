def login_disponivel(lg, lt):
    c = 1
    a = lg
    vai = True
    if lg not in lt:
        return lg
    while vai:
        for i in lt:

            if lg not in lt:
                vai = False
                return lg


            if i == lg:
                lg = a
                lg = lg + '{0}'.format(c)
                c +=1
                
            
    return lg