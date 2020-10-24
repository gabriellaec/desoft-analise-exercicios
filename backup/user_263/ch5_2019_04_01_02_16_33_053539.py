def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n%2==0 and n!=2:
        return False
    else:
        i=3
        primo=True
        while i<n:
            if n%i==0:
                primo=False
            i+=2
        if primo==True:
            return True
        else:
            return False
def maior_primo_menor_que(n):
    primo=eh_primo(n)
    if primo==True:
        return n
    elif n<=1:
        return -1
    else:
        num=3
        maior=0
        while num<n:
            if eh_primo(num)==True:
                maior=num
            num+=2
        return maior
        