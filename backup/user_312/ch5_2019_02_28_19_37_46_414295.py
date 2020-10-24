def maior_primo_menor_que(n):
    i=1
    primo=0
    while i<n:
        if n%i!=0:
            primo+=1
        i+=1
    if primo > 2:
        return False
    else:
        return True
