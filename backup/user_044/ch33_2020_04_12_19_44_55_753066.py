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
 
def lista_primos(n):
    i=0
    ls=[]
    while len(ls)!=n:
        if eh_primo(i):
            ls.append(i)
        i+=1
    return ls    

def primos_entre(a,b):
    