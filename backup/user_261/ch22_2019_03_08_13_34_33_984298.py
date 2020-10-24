def eh_bissexto(ano):
    if ano%400==0:
	    return "true"
    elif ano%100==0:
        return "false"
    elif ano%4==0:
        return "true"
    else:
        return "false"
