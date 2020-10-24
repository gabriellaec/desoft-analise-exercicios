def teste(n):
    primo=True
    i=2
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo
def maior_primo_menor_que(n):
    i=n
    i-=1
    while i>1:
        if n%i!=0:
            i-=1
    return i
            




        

        