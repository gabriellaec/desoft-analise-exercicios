def fatorial(x):
    y=1
    f=1
    while y>0:
        y=x*f
        f+=x-1
    return y