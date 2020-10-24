def login_disponivel(lg, lt):
    c = 1
    a = 0
    if lg not in lt:
        return lg
    for i in lt:
        
        if i == lg:
            a = lg + '{0}'.format(c)
        c +=1
            
    return a
        
            

        