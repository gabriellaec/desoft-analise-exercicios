def ft(t,n):
    z=(n*(0.00694444))*(t*360)
    return z
t=int(input('tempo em anos'))
n=int(input('cigarros por dia'))
print((ft(t,n)),('anos perdidos'))