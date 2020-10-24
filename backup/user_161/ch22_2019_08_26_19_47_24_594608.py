def eh_bissexto(x):
    if (x%100)==0 and x%400!=0:
        return False
    elif x%4==0:
        return True
    else:
        return False