def eh_primo(p):
    i=0
    if p==1:
        return False
    while p>0:
        for y in range(1,p+1):
            if p%y==0:
                i+=1
        if i<=2:
            return True
        else:
            return False