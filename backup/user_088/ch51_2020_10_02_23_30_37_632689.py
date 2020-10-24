def eh_primo (x):
    if(x==2):
        return True
    elif (x==0 or x==1 or x%2==0):
        return False        
    else:
        n = 3
        while (n < x):
            if x%n==0:
                return False
            n += 2
        return True
def primos_entre(a,b):
    primos= []
    while a<=b:
        n=eh_primo(a)
        if (n and n!=-1):
            primos.append(a)
        a+=1
    return primos