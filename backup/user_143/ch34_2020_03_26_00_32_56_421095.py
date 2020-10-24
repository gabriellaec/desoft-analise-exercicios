def eh_primo (perg):
    if perg==1 or perg==0:
        return False
    elif perg==2:
        return True
    elif perg>1:
        if perg%2==0:
            return False
        else:
            impar=3
            invalid=True
            while invalid:
                if impar<perg and perg%impar ==0:
                    return False
                elif impar==perg:
                    return True
                    invalid=False
                impar+=2
def maior_primo_menor_que (n):
    p=0
    if n<=1:
        p=pr
        pr=-1
    while p<=n-1 and p>1:
        p+=1
        if eh_primo(p):
            p=pr
            pr+=1
    return pr