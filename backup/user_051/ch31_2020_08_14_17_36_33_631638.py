def eh_primo(X):
    if X%2==0:
        return False
    Z=3
    while Z<X:
        if X%Z==0:
            return False
        Z+=2
    return True