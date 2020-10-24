def eh_bissexto(ano):
	if ano==1:
		return True
    if (ano%4)==0:
		return True
	if (ano%100)==0:
		return False
	