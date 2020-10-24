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

def verifica_primos(lista):
    primo = {}
    for numeros in lista:
        if eh_primo(numeros):
            primo[numeros] = True
        else:
            primo[numeros] = False
    return primo
            
     