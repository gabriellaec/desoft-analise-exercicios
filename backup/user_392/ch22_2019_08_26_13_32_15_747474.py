def eh_bissexto(x):
    bisex = True
    if x%100 == 0:
    	bisex = False
    if not x%4 == 0:
        bisex = False
    if x%400 == 0:
        bisex == True
    return bisex 