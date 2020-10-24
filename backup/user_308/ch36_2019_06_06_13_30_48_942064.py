def eh_primo(x):
    primo=True
    if x<=1:
        primo=False
    for e in range (2,x):
        if x%e==0 and e!=x:
            primo=False
    return primo