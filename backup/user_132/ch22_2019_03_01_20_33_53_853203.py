def eh_bissexto(a)
	if a%400==0:
    	return true
    elif a%100 == 0:
    	return false
    elif a%4 == 0:
    	return true
    else:
        return false