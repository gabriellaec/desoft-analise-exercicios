def eh_primo(n):
    if n <= 1:
        return False
    
    np = 3
    while np < n:
        
        if n%2 == 0 or n%np == 0:
            return False
        np +=2
    return True 

def lista_primos(n):
    pos = 1
    num = 3
    lista = []
    if n > 0:
        lista.append(2)
        while pos != n:
            if eh_primo(num) == True:
                lista.append(num)
                pos += 1
                num+=1
            else:
                num+=1
        return lista        
    else:           
        return lista  