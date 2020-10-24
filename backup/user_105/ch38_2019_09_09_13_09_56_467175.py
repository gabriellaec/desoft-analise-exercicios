def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n=n+2
        else: 
            return True

def lista_primo():
    primos=[]
    i=1    
    while i<100:
        if eh_primo (i) == True:
            primos.append(i)
        i+=1
    return primos
            