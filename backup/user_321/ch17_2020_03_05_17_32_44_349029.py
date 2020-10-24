def eh_bissexto (ano):
    if (ano%4==0):
        return True
    elif (ano%4!=0):
        return False
    elif (ano==100):
        return True