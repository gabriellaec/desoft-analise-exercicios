def maior_primo_menor_que(n):
    primo=True
    i=2
    if n==1 or n==0:
        return -1
    while i<n:
        if n%i==0:
            return -1
        i+=1
    return primo

def maior_primo_menor_que(n):
    i=n
    i-=i
    while i>1:
        if n%i!=0:
            i-=1
    return i
            




        

        