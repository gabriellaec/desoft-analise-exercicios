def maior_primo_menor_que(n):
    primo=true
    i=2
    while i<n:
        if n%i==0:
            primo=false
        i+=1
    return primo
    