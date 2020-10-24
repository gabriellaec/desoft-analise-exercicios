def eh_bissexto(z):
    if z%400== 0:
        return true
    elif z%400 != 0 and z%100==0:
        return false
    elif z%4 == 0:
        return true
    else:
        return false
print(eh_bissexto(z))
