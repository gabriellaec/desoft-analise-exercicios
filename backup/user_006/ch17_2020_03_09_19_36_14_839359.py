def eh_bissexto(ano):
	if ano%100==0 and ano%400==0:
        return "True"
    elif ano%4==0:
    	return "True"
    else:
        return "False"
        