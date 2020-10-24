def arcotangente (x, n):
    cont=1
    a=3
    b=3
    c=-1
    for cont in range(0,n):
        x+=c*(x**a/b)
        a+=2
        b+=2
        c*=-1
        cont+=1
    return x

        
    