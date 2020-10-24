def eh_bissexto(ano):
    while ano>1:
    	if ano % 400 == 0:
        	eh_bissexto=True
    	elif ano % 100 == 0:
    	    eh_bissexto=False
    	elif ano % 4 == 0:
        	eh_bissexto = True