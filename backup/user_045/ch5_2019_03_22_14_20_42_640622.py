def maior_primo_menor_que(n):
    i=n
    while i>1:
        i-=1
        if n%i==0:
            break
    return i
         
        

        