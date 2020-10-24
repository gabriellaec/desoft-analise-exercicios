def eh_primo(n):
    if n ==1 or n ==0:
        return false
    elif n==2:
        return true
    else:
        if n%2==0:
            return false
        else:
            impar = 3
            while impar <n:
                if n%impar==0:
                    return false
                impar= impar +2
            return true
        
def primos_entre(a,b):
    p=0
    while b-a>=0:
        while eh_primo(a) == false and b-a >0:
            a+=1
        if eh primo(a) == true:
            p=p+1
        a=a+1
    return p