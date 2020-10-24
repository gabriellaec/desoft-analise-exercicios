def fatorial(x):
    y=0
    f=1
    while x>0:
        y=x*f
        f+=x-1
    print(fatorial(3))