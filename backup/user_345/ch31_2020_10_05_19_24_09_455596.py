def eh_primo(n):
    primo = True
    if (n == 0)or (n == 1):
        primo = False
    if n > 2:
        if n % 2== 0:
            primo=False
        else:
            x =3
            while(x < n):
                if n % x == 0:
                    primo = False 
                    x+=2
    return eh_primo