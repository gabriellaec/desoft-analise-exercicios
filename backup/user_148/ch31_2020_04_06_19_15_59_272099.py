def eh_primo(p):
    i = 1
    while i<p:
        if p%i==0:
            i+=1
            return True
        else:
            return False