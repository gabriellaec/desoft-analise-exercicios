def eh_primo(n):
    primo = True
    a = 2
    if n == 0 or n == 1:
        return False
    while a<n:
        if n%a == 0:
            return False
        a+=1
        
    return True

def lista_primos(n):
    lista = []
    num = 0
    while num < n:
    	if eh_primo(i) == True:
        	lista.append(eh_primo(n))
        	i += 1
            num = num +1
        else:
            i += 1
            n += 1