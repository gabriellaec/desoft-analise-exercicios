def eh_bissexto(ano):
    if int(ano/4) == ano/4:
        if int(ano/100) == ano/100:
            if int(ano/400) == ano/400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False