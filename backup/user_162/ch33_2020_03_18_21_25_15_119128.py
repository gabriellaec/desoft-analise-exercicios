def eh_primo(p):
    if p <= 1:
        return False
    
    np = 3
    while np < p:
        
        if p%2 == 0 or p%np == 0:
            return False
        np +=2
    return True 


def primos_entre(a, b):
    lista = []
    while b >= a:
        if eh_primo(b)==False:
            b-=1
        else:
            lista.append(b)
            b-=1
    return len(lista)