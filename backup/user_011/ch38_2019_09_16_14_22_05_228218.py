def eh_primo(num):
    a = 2
    if num == 0 or num == 1:
        return False
    while a<num:
        if num%a == 0:
            return False
        a+=1
        
    return True

def primos_entre(a,b):
    n = a
    q = 0
    while n<=b:
        if eh_primo(n) == True:
            q += 1
        n += 1
    return q