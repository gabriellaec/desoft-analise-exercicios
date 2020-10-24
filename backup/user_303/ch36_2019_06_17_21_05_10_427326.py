def eh_primo(k): 
    c=2
    p=True
    if k == 0 or k == 1:
        p=False
    while c<k:
        if k%c==0: 
            p=False 
        c+=1
    return p    