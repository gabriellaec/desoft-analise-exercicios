def eh_primo (x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    elif x>2:
        if x%2==0:
            return False
        else:
            y=3
            a=True
            while a:
                if x>y and x%y==0:
                    return False
                elif x==y:
                    return True
                    a=False
                y=y+2
                
def maior_primo_menor_que(n):
    i=0
    while i<=n:
        if eh_primo(i)>0 and max(i)<=n:
            return i
        else:
            i+=1
            return -1
                