def eh_bissexto(y):
    k=y%100
    r=y%400
    p=y%4
    if r==0 and k!=0 and p==0:
        return True
    else:
        return False