def eh_bissexto(y):
    z=y%4
    k=z%100
    if z==0 and k==0:
        return True
    else:
        return False