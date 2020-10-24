def login_disponivel(user,exist):
    c=0
    i=0
    if user not in exist:
        return user
    else:
        while c<len(exist):
            if exist[c]==user:
                i+=1
                k=str(i)
                return (user+k)
            c+=1