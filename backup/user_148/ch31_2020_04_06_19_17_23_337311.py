def eh_primo(p):
    i = 1
    while i<p:
        if p%2==0 and p%i==0:
            i+=2
            return True
        else:
            return False