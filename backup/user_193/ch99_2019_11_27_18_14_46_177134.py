def login_disponivel(user,exist):
    if user not in exist:
        return user
    else:
        c=0
        i=0
        while c<len(exist):
            if exist[c]==user:
                i+=1
                k=str(i)
                return (user+k)
            c+=1