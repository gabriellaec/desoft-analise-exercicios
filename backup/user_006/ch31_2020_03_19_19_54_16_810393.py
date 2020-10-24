def eh_primo(numero):
	if numero==2:
		return True
	else:
		if numero%2==0:
			return False
		else:
			i=1
			while i<numero:
				if numero%(numero-2*i)==0:
					return False
				else:
					i=i+1
			return True
            	
        	