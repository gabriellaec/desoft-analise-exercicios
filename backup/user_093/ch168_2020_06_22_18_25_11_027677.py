def login_disponivel(login,lis):
    if not login in lis:
        return login
    i=1
    else:
        while True:
            login2=login+str(i)
            if not login2 in lis:
                return login2
            i+=1
           
        
        