def verifica_primo(k): 
    c=2
    p=True
    while c<k:
        if k%c==0: 
            p=False 
        c+=1
    return p    
def maior_primo_menor_que(n):
    c=n
    while c>=2:
        if verifica_primo(c):
            return c 
        c-=1
    return -1