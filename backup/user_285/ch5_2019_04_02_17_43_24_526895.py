def maior_primo_menor_que(n):
    for i in range(2,n):
        x=0
        for k in range(2,n):
            if i%k==0:
                x+=1
        if x<=1:
            primo=i
    return primo

   