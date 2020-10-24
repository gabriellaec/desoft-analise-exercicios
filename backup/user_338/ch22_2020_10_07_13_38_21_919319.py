def reducao(n,a):
    r=365*a*n/144
    return r
n=float(input('digite o numero de cigarros que fuma por dia'))
a=float(input('digite a quantos anos fuma'))

c=reducao(n,a)
print('o tempo de vida perdido em dias e {0}'.format(c))