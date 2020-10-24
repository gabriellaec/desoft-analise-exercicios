def eh_primo(x):
    if x==1 or x==0: 
        return False
    elif x==2 or x==3:
        return True
    elif x%2==0:
        return False
    i=3
    while i<x:
        if x%i==0:
            return False
        i+=2
    return True

n=int(input("fale um número: "))       
def maior_primo_menor_que(n):
    y=n
    while y<=n:
        if eh_primo(y)==True:
            return y
        y-=1
    return -1