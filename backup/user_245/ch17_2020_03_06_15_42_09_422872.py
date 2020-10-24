def eh_bissexto(ano):
    y = ano%4
    if y == 0:
        print ("True")
    else:
        print ("False")
    return y