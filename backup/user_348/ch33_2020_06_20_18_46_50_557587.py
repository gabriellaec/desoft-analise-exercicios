def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range (3, n, 2):
        if (n%2==0):
            return False 
        elif(n%i == 0):
            return False
    else:
        return True
    
def primos_entre (a,b):
    contador = 0
    p = eh_primo(n)
    while p >= a and p<=b:
        contador = contador + 1
    return contador
    