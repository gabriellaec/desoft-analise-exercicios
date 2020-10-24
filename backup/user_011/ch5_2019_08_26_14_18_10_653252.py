def maior_primo_menor_que(num):
	primo = True
	a = 2
	while a < num:
    	if num%a == 0:
        	primo = False
        
    a+=1
	return(primo)