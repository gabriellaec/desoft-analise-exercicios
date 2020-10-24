def eh_primo(p):
    if p == 0 or p==1:
        return False
    while c in range(2, p):
        if p % 2 != 0 or p == 2:
            if p % c == 0:
                return False
    return True
def primos_entre(a,b,p):
    num = 0
    for p in range (a, b+1):
        if eh_primo(c):
            num+=1
    return num
    
   

