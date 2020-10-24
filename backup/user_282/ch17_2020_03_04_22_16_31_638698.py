def eh_bissexto(Ano):
    if (Ano%4 == 0 and Ano%100 != 0) or Ano%400 == 0:
        return True
    else:
        return False


a = int(input('Ano: '))
print(eh_bissexto(a))