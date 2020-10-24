def login_disponivel(lg, lt):
    c = 1
    a = lg
    if lg not in lt:
        return lg
    for i in lt:
        
        if i == lg:
            lg = a
            lg = lg + '{0}'.format(c)
            c +=1
            
    return a
        
            

        