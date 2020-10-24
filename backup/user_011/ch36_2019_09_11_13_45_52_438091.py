def eh_primo(n):
    a = 2
    primo = True
    while a < n:
        if n%a == 0:
            primo = False
            a+=1
        return primo