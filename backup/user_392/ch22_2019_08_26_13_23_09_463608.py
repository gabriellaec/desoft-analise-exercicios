def eh_bissexto(x):
    bisex = True
    if not x%4 == 0:
        bisex = False
    if x%100 == 0:
        bisex = False
    elif not x%400 == 0:
        bisex == False
    return bisex 