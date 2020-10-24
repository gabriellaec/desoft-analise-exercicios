def eh_primo(k): 
    c=2
    p=True
    while c<k:
        if k%c==0: 
            p=False 
        c+=1
    return p    