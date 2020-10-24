def eh_bissexto(x):
    if x >= 400:
        x%400 ==0
	elif x%100 != 0 and x%4 == 0:
        return True
    else:
        return False
    