def eh_bissexto(ANO):
    if z%400== 0:
        return true
    elif z%400 != 0 and z%100==0:
        return false
    elif z%4 == 0:
        return true
    else:
        return false
