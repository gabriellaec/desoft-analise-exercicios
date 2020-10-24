def fatorial(x):
    y=1
    f=1
    while y>0 and f>=1:
        y=x*f
        f+=x-1
    print(fatorial(3))