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


def  lista_primos(n):
    i = 0
    nova =[]
    while i < n:
        if eh_primo(i):
            nova.append(i)
        i += 1
    print (n)
    print (nova)
    return nova
   
        
        