def eh_bissexto(a):
    if a%4==0 and a%100!=0:
        return True
    elif a%400!=0:
        return True
    else:
        return False


