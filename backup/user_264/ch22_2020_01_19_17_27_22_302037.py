def eh_bissexto(ano):
    y = ano % 4
    if y == 0:
        return "ano bissexto"
    else:
        return "ano não bissexto"
    return y

test = eh_bissexto(int(input("insira um ano:")))   
print (test)     