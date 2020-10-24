def login_disponivel(username,lista):
    if username not in lista:
        return username
    else:
        trying = True
        n = 1
        while trying:
            username += str(n)
            if username not in lista:
                trying = False
                return username
            else:
                n += 1
        
        
            