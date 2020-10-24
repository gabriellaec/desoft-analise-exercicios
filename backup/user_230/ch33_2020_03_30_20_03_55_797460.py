def eh_primo(n):
    div=3
    if n%2==0 and n!=2 or n==1 or n==0:
        return False
    while n > div:
        if n%div==0:
            return False
        div +=2
    return True

def primos_entre(a,b):
    n_primos=0
    while a<=b:
        if eh_primo(a):
            n_primos +=1
        x+=1
    return n_primos