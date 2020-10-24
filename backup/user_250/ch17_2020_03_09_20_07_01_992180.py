def eh_bissexto(y):
    z=y%4
    k=y%100
    p=y%4
    if z==0 and k!=0 and p==0:
        return True
    else:
        return False