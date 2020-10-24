def eh_primo(x): 
    if x==1 or x==0:
        return (False)
    if x==2:
        return (True)
    if x%2==0:
        return (False)
    a=3
    while a<=x:
        a+=1
        if x%a==0:
            return (False)
    return (True)