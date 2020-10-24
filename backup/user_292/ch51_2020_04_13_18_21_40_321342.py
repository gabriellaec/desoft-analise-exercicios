def primos_entre(a,b):
    x = []
    for i in range(a,b+1):
        if i==2:
            x += [i]
        else:
            d=3
            while i%d!=0 and i>d:
                d=d+2
            if i==d:
                x += [i]
    return x