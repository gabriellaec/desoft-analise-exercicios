def eh_bissexto(a):
    if a%4==0:
        return True
    elif a%100!=0 or a%400==0:
        return True
    else:
        return False
a=input('ano?')

