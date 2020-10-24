def    eh_primo(x):
    if x<2:
        return False
    elif x==2 or x==3 or x==5 or x==7:
        return True
    else:
        t=2
        i=3
        y=5
        j=7
    while (t<x):
        if x%t==0 or x%i==0 or x%y==0 or x%j==0:
            return False
        else:
            return True
print(eh_primo(29))