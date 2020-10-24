def lista_primos(num):
    i=1
    k=0
    primo=[0]*num

    while primo[num] == [0]:
        j=2
        c=0
        while j <= i:
            if i % j == 0:
                c=c+1
            j=j+1
        if c == 0:
            primo[k]=i
        i=i+1
        k=k+1