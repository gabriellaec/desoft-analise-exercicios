def primos_entres(a,b):
    x=0
    for i in range(a,b,1):
        if i==2:
            x+=1
        else:
            d=3
            while i%d!=0 and i>d:
                d=d+2
            if i==d:
                x+=1
    return x