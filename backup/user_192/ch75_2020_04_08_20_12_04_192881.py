def eh_primo(x):
    if x==2:
        return True
    elif x==0 or x==1:
        return False 
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
            	return False
            n += 2
        return True

def verifica_primos(numeros):
    primo = {}
    for n in numeros:
        def eh_primo(x)
    return primo 