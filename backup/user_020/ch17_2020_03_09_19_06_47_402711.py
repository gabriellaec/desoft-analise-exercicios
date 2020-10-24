def eh_bissexto(n):
    if n % 4 == 0 and n % 400 == 0 and n % 100 != 0:
        return True
    else:
        return False
print(eh_bissexto(100))