def eh_bissexto(x):
    if (x%400 == 0):
       return True
    elif (x%400!= 0) and (x%100 == 0):
    	return False
    elif (x%400!= 0) and (x%100!= 0) and (x%4 == 0):
    	return True
    else:
    	return False