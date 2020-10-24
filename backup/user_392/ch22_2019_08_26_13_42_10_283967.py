def eh_bissexto(x):
    bisex = False
    if x%400 == 0:
        bisex == True
    else:	
        if x%100 == 0:
    		bisex = False
    if x%4 == 0:
        bisex = True
    return bisex