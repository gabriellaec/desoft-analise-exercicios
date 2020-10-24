def eh_bissexto(ano):
    resto = ano%4
    if resto ==0:
        return True
    else:
        return False
