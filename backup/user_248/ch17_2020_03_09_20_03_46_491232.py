def eh_bissexto(ano):
    resto=ano%4
    if(resto==0):
        return True
    elif ano%400==0:
        return True
    elif ano%100==0:
        return False
    else:
        return False
print(eh_bissexto(3))