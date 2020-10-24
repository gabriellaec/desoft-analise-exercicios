def eh_bissexto(a)
	if a%400 == 0
    return True
	elif (a%400 != 0) and (a%100 == 0)
    return False
	elif (a%4==0)
    return True
print (eh_bissexto(2004)