def login_disponivel(login,lis):
    if not login in lis:
        return login
    
    else:
        i=1
        while True:
            login2=login+str(i)
            if not login2 in lis:
                return login2
            i+=1
           
        
        