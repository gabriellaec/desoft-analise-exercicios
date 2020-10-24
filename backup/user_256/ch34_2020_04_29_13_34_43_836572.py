def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(3, n, 2):
        if n%2==0:
            return False
        elif n%i==0:
            return False
    else:
        return True
    
def  maior_primo_menor_que(n):
    p = -1
    lala = True
    
    while n>0 and lala:
        if n ==2:
            p = 2
            lala = False
        elif eh_primo(n):
            p = n
            lala = False
      
        n = n-1
    print (p)
    return p
    
    
    
    