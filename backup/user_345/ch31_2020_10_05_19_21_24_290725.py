def eh_primo(n)
    eh_primo = True
    if (n == 0)or (n == 1):
        eh_primo = False
        return (eh_primo) 
    elif n == 2:
            return (eh_primo)
    if n > 2:
        if n % 2== 0:
            eh_primo=False
            return(eh_primo)
        else:
            x =3
            while(x < n):
                if n % x == 0:
                    eh_primo = False 
                    x+=2
                    return (eh_primo)
            if x==n:
                return (eh_primo)