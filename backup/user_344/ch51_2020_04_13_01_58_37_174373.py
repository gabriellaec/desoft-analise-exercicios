def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    elif numero % 2 == 0:
        return False
    n = 3 
    while n< numero:
        if numero % n == 0:
            return False
        n+=2
    return True
    
def primos_entre(a,b,p):
    lista=[]
    while p > a and p< b:
        if eh_primo(p) == True:
            lista.append(p)
    return lista
   
        
    
    