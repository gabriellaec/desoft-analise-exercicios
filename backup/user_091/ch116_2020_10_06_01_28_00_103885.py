def raiz_quadrada(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2**(1/2)
    
    else:
        i=2
        max=0
        while i<n:
            max=n-i
            i+=1
        if max==0:
            return i
        elif max!=0:
            return n**(1/2)
    
        