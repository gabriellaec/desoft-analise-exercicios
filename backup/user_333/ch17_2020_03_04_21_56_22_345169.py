def eh_bissexto(ano):
    if ano % 4==0:
        if ano % 100==0 and ano%400==0:
            return True
        elif ano % 100==0:
            return False
        else:
            return True
    else:
        return False
    
ano=int(input('ano: '))
print(eh_bissexto(ano))
        