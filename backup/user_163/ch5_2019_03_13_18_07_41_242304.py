def is_primo(num):

    i = 2
    check = 0

    while(i<num):
		
        i = 1 + i
        check += num % i

    if(check == 0):

        return(1)

    return(0)

def maior_primo_menor_que(num):
	
    if(num <= 0):
        
        return(-1)
    
    i = 0
    low = 0

    while(i < num):
		
        i = 1 + i
        
        if(is_primo(i) == 1):

            low = i

    return i
