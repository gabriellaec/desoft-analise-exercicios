def eh_primo (x):
    if x==1 or x==0:
        return False
    if x==2:
        return True 
    if x%2 == 0:
        return False 
    a=3
    while a<x:
        if x%a==0:
            return False
        a= a + 1
    return True 
    
def primos_entre(inicio, fim):
    contador = 0 
    x = inicio 
    while x <= fim:
        if eh_primo(x): 
            contador += 1
        numero += 1
    return contador 

