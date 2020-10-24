def login_disponivel(username,lista):
    if username not in lista:
        return username
    else:
        n = 1
        username += str(n)
        trying = True
        while trying:
            if username not in lista:
                return username
            else:
                n += 1
                username[-1] = str(n)
        
            