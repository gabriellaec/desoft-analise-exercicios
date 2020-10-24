def eh_bissexto(ano):
    if ano/400==int(ano/400):
        return True
    elif ano/100==int(ano/100):
        return False
    elif ano/4==int(ano/4):
        return True
    else:
        return False