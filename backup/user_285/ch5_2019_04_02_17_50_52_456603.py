def maior_primo_menor_que(n):
    for i in range(1,n):
        x=0
        for k in range(1,n):
            if i%k==0:
                x+=1
        if x<=2:
            primo=i
    if primo<=1:
        primo=-1
    return primo       