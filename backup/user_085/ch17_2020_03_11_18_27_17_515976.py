a = int(input('Digite o ano: '))
def eh_bissexto(a):
    if a%4 == 0:                     #1
        if a%100 == 0:               #2
            if a%400 == 0:           #3
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(eh_bissexto(a))