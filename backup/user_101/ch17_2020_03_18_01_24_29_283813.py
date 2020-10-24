def eh_bissexto (num):
    if num%400==0:
        return True
    elif num%100!=0 and num%4==0:
    	return True
    else:
        return False
    