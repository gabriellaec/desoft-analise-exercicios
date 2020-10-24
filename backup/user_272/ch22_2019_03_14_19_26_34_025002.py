def eh_bissexto(ano):
    if ano%100!=0 and ano%4==0:
	return 'Eh um ano bissexto'
	elif ano%400==0:
	return 'Eh um ano bissexto'
	else 
    return 'Nao eh bissexto'