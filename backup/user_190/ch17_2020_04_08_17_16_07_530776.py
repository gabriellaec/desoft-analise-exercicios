def eh_bissexto(a):
    x=a
    if x%4==0 and x%100!=0:
        return True
    else:
        return False    