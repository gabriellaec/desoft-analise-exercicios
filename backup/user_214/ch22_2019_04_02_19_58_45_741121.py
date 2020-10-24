def eh_bissexto(ano):
    x="nada"
    if ano % 4 == 0:
    	if ano % 100 == 0 and ano % 400 != 0:
        	x="False"
    	else:
        	x="True"
	return x