def login_disponivel(lg, lt):
    c = 1
    a = lg
    a = 0
    vai = True
    if lg not in lt:
        return lg
    while vai:
        for i in lt:
            a+=1
            if a >= len(lt):
                vai = False

            if i == lg:
                lg = a
                lg = lg + '{0}'.format(c)
                c +=1
                
            
    return lg