def eh_primo(n):
    i=2
    if n==0 or n==1:
        return False
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True


def primos_entre(a, b):
    
    quantidade_primos=0
    a=a
    
    while a<=b:
        if eh_primo(a):
            quantidade_primos+=1
        a+=1
    
    return quantidade_primos