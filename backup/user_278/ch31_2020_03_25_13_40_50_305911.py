def eh_primo(x): 
    if x<=1:
        return (False)
    if x==2:
        return (True)
    if x%2==0:
        return (False)
    a= 3
    while a<x:
        if x%a==0:
            return (False)
        else:
            a+=2
    return (True)