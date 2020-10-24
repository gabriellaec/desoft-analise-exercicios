def eh_primo(n):
    eh_primo = True
    if (n == 0)or (n == 1):
        eh_primo = False
    if n > 2:
        if n % 2== 0:
            eh_primo=False
        else:
            x =3
            while(x < n):
                if n % x == 0:
                    eh_primo = False 
                    x+=2
                    return (eh_primo)
    return eh_primo