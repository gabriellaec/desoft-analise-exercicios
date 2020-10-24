def eh_primo(x):
    primo=True
    for e in range (2,x):
        if x%e==0:
            primo=False
    return primo