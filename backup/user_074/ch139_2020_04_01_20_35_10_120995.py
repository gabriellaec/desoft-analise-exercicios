def arcotangente(x):
    x=0
    a=0
    b=0
    c=0
    while x>0:
        a*=a
        b*=b
        c*=c
        a=-(x**3)/3
        b=(x**5)/5
        c=-(x**7)/7
        y=x+a+b+c
        print(y)
    