def eh_bissexto(a):
    y = a%4 and y = a%400 and y!=a%100
    if y==0:
        return 'True'
    else:
        return 'False'