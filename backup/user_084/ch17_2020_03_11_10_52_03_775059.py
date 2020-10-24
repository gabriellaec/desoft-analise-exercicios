def eh_bissexto(x):
	if x%4==0:
		return(True)
    elif x%100==0 and x%400!==0:
		return(False)
	else:
		return(False)
