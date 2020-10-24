def eh_primo(num):
    div = 3 
    if num % 2 == 0 and num != 2 or num == 1 or num == 0:
        return False
    
    while num > div:
        if num % div == 0:
            return False
        div += 2 
    return True 

def lista_primos(n):
    lista = []
    t = 0 
    i = 0 
    while n > t:
        if eh_primo(i) == True:
            lista.append(i)
            t += 1
        i += 1
    return lista