def confere_primo(nu):
    i=2
    while i<nu:
        if nu%i==0:
            return False
        i+=1
    return True

def maior_primo_menor_que (n):
    i=n-1
    ii=0
    if n<2:
        return -1
    if confere_primo(n):
        return n
    else:
        while ii < n:
            if confere_primo(i):
                return i
            else:
                i-=1
                ii+=1
            return -1
            
            
            
    
    