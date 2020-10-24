def tempo_vida(c,a):
    y=c*0.006945*365*a
    return y
c=int(input('cigarros por dia?'))
a=int(input('quantos anos?'))
x=tempo_vida(c,a)
print(x)