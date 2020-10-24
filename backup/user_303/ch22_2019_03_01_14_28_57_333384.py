def eh_bissexto(x)
	if x%400==0:
    	return True
    elif x%100==0:
    	return False 
    elif x%4==0:
    	return True
    else: 
        return False 
a=int(input("Escreva o ano aqui:"))
print (eh_bissexto(a))
