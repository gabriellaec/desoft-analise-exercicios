def eh_bissexto(a):
    b=abs(a-2020)
    if b%4==0 and b%100!=0:
        return True
    else:
        return False