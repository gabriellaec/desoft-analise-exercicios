def eh_bissexto(ano):
    if ano%4==0:
        return True
    else:
        return False
a=int(input('Digite um ano'))
print(eh_bissexto(a))