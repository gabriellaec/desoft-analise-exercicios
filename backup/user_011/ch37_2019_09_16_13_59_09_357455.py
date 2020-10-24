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

def lista_primos(num):
    lista = []
    num = 2
    while len(lista)<=num:
    	if eh_primo(n) == True:
        	lista.append(n)
        num = num +1
            
    return lista 