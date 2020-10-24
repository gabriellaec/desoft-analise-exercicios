def eh_bissexto('ano'):
    if ano//400:
        return True
    elif ano//100:
        return False
    else:
        return True