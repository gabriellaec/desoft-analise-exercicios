def eh_bissexto(ano):
	if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    	return "Ano bissexto"
	else:
    	return "Não é bissexto"

    