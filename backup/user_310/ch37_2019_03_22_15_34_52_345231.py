def imprime_primos(a):
    
    def eh_primo(n):
        i=2
        if n==0 or n==1:
            return False
        while i<n:
            if n%i==0:
                return False
            i+=1
        return True
    
    c=2
    
    while c<=a:
        if eh_primo(c):
            print (c)
        c+=1
            