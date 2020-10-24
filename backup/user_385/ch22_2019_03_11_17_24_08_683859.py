def eh_bissexto(a):
    y = a%4 and a%400 and a!= a%100
    if y==0:
        return 'True'
    else:
        return 'False'