def eh_bissexto(Ano):
    if Ano%4 == 0 and Ano%100 != 0:
        return True
    elif Ano%400 == 0:
        return True
    else:
        return False


print(eh_bissexto(2018))