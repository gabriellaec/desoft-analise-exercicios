def eh_bissexto(x):
	if (x%4==0 and x%100!=0) or (x%400==0):
        print ("Bissexto")
	else:
        print ("Não é bissexto")