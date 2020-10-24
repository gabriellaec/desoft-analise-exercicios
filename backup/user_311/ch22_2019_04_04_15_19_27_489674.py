def eh_bissexto(ano):
    if ano % 4 == 0:
        return True
    else:
        return False
    
x = 2020
print (eh_bissexto(x))