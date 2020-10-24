def eh_bissexto(ano):
    if ano/100==int(ano/100):
        return True
    elif ano/4==int(ano/4):
        return True
    else:
        return False