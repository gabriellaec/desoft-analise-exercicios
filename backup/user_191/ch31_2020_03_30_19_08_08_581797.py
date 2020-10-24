def eh_primo(n):
    f=1
    if (n==0):
        return(1>2)
    elif n==1:
        return(1>2)
    elif n==2:
        return(1<2)
    elif n%2==0:
        return(1>2)
    elif (f<n):
        while f<n:
            if n%f==0:
                return(1>2)
            else:
                f=f+2
    elif n==1:
        return(1>2)
    else:
        return(1<2)