def primos(p):
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


def maior_primo_menor_que(n):
    if n<2:
        return -1
    elif primos(n)==True:
        return n
    while primos(n)==False:
        n=n-1
        if primos(n)==True:
            return n
