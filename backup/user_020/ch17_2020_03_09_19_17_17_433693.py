def eh_bissexto(n):
    if n % 4 >= 0:
        return True
    elif n % 100 != 0:
        return True
    else:
        return False
print(eh_bissexto(4))