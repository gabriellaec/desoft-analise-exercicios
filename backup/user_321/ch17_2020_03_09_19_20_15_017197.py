def eh_bissexto (ano):
    if (ano==1):
        return False
    elif (ano%4==0) and (ano%100!=0):
        return
    elif (ano%400==0):
        return
    else:
        return