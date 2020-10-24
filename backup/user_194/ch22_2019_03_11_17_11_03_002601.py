def eh_bissexto(a):
    y = a % 4 and a > 1
    if y == 0:
        return 'True'
    else: 
        return 'False'