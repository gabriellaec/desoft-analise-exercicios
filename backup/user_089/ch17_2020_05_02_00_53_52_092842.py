def eh_bissexto(a):
    if a < 400:
        if a < 100:
            if a % 4 == 0:
                return True
            else:
                return False
        else:
            if a % 4 == 0 and a % 100 != 0:
                return True
            else:
                return False
    else:
        if a % 4 == 0 and a % 100 != 0 and a % 400 == 0:
            return True
        else:
            return False