def eh_primo (x):
    if x==2:
        return True
    elif x==0 or x==1:
        return False        
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n += 2
        return True
def maior_primo_menor_que(n):
    a=1
    maior=-1
    while(a<=n):
        if eh_primo(a)==True
            maior=a
        a+=1
    return maior