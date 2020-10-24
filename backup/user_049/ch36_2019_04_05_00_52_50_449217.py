def eh_primo(n):
    primo=False
    if n<=1:
        return primo
    elif n==2:
        return (not primo)
    else:
        if n%2==0:
            return primo
        else:
            for i in range(3,n,2):
                if n%i==0:
                    return primo
            return (not primo)

            