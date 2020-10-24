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
    
def primos_entre(a,b):
    p=[]
    n=a
    for num in range(a,b):
        if eh_primo(num) == True:
            p.append(num)
    return p 