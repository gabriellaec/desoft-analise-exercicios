def eh_primo (n):
    if n == 2:
        return True 
    elif n == 0 or n == 1:
        return False 
    elif n%2 == 0:
        return False 
    else:
        contador = 3
        while contador < n:
            if n%contador == 0: 
                return False 
            contador +=2
        return True 
    
def maior_primo_menor_que (n):
    x=n
    if eh_primo==True:
        return n
    while x>=2:
        if eh_primo(x):
            return x
        x -=1
        
    if x<2:
        return -1