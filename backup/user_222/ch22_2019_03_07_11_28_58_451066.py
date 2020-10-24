def eh_bissexto(a):
    if a%4==0:
        return True
    else:
        return False
a=int(input('ano'))
print(eh_bissexto(a))
