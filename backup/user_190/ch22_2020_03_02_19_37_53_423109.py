def cigarros (d,a):
    c=(d*365*a)/144
    return c
r=int(input('quantos cigarros você fuma por dia?: '))
g=int(input('há quantos anos você fuma?: '))
j= cigarros (r,g)
print (j)