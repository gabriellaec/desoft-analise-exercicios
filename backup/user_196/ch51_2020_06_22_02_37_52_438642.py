def eh_primo (num):
	i=2
	if num == 2:
		return True
	elif num == 0 or num == 1:
		return False
	while i < num:
		if num % i == 0:
			return False
		i = i+1
	return True

def primos_entre(a,b):
    i=0
    p = []
    while i < a and i > b:
        if eh_primo(i):
            p.append(i)
            i+=1
        else:
            i+=1
    return (len (p))    
