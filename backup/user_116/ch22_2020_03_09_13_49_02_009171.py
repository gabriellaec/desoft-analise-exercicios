def ft(t,n):
    z=(n*(t*360)*(0.00694444))
    return z
t=int(input('tempo em anos'))
n=int(input('cigarros por dia'))
print('{0} anos perdidos'.format(ft(t,n))
