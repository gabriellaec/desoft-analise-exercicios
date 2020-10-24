def eh_primo (x):
    if x <= 1:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
       
    return True

def primos_entre (a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista.append(i)
    return lista