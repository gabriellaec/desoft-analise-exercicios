def numero_digitos(s):
    digito=0
    for i in s:
        if i.isdigit()==True:
            digito+=1
	return str(digito)