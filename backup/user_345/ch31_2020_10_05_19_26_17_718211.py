def eh_primo(n):
    primo = True
    if n<2:
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
    return primo