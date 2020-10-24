def eh_primo(numero):
    contador=1
    while contador< numero:
    	if numero%2 != 0 or numero == 2:
        	if numero%contador != 0:
        		contador+= 2
        else: 
        	numero_primo = False  	
       
    return numero_primo