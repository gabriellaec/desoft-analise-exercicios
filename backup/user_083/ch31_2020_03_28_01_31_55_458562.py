def    eh_primo(x):
    if x<2:
        return False
    elif x == 2:
        return True
    else:
        t=2
        i=3
    while (t<x):
        if x%t==0 or x%i==0:
            return False
            t+=1
            i+=1
        else:
            return True
print(eh_primo(21))