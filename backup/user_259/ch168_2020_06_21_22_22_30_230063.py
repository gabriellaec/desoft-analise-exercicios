def login_disponivel(username,lista):
    if username not in lista:
        return username
    else:
        n = 1
        new_username = username + str(n)
        trying = True
        while trying:
            if new_username not in lista:
                return new_username
            else:
                n += 1
                new_username = username + str(n)
        
            