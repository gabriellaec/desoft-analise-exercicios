def eh_bissexto(ano):
	if ano%4 == 0 and not ano%100 == 0 and not ano%400 == 0:
		return(True)
	else:
		return(False)
    
print(eh_bissexto(2020))