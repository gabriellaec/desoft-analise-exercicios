def eh_primo(n):
    b=2
    z=True
    if n==2:
        return True
    elif n==0 or n==1:
        return False
    else:
        while b!=n and z:
            a=n%b
            b+=1
            if a==0:
                z=False
                return False
            elif b==n and a!=0:
                return True
def maior_primo_menor_que(n):
    x=True
    num=n
    if n<=1:
        x=-1
        return x
    else:
        while x:
            if eh_primo(num)==True:
                x=False
            else:
                num-=1
    return num        
    
    
    
    
    
    
    
    
    
    
    
    
    
    