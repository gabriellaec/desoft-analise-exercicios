def eh_primo(n):
    primo = True
    a = 2
    while a<n:
        if n%a == 0:
            return False
        a+=1
         