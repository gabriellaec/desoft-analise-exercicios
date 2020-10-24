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

def maior_primo_menor_que (n):
    contador = 0
    p = eh_primo(n)
    maior_primo = 0
    while p <= n:
        if eh_primo(p) > maior_primo:
            maior_primo = eh_primo(p)
        p = p + 1
    return maior_primo
    
