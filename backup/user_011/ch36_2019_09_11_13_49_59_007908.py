def eh_primo(num):
    primo = True
    a = 2
    if num == 0:
        return False
    while a < num:
        if num%a == 0:
            primo = False
        a+=1
    return primo