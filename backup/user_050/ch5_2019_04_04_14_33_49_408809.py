def eh_primo(x):
	if x<2:
		return False
	contador = 2
	while contador<x:
		if x % contador == 0:
			return False
		contador +=1
	return True

def maior_primo_menor_que(x):
    if x > 1:
        while not eh_primo(x):
            x -= 1
        return x
    else:
        return -1