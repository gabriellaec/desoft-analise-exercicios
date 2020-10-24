def eh_primo(n):
    a = 2
    primo = True
    while a < n:
        if n%a == 0:
            primo = False 
            return primo
        a+=1
        