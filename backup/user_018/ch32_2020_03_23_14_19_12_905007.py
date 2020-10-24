def eh_primo (x):
    if x == 2:
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
lista = []
def lista_primos(eh_primo,n):
    while len(lista)<n:
        if eh_primo(x) == True:
            lista.append(x)
    return lista 