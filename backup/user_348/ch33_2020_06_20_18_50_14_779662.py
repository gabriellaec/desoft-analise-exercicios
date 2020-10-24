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
    p = 2
    while p >= a and p<=b:
        if n == 2:
            contador += 1
        for i in range (3, b, 2):
            if (p%2 !=0) and (p%i != 0):
                contador += 1
    return contador
    