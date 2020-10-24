def cigarros (c,a):
    v=(c*365*a)/144
    return v
y=int(input('quantos cigarros fuma?:'))
o=int(input('quantos anos fuma?:'))
d= cigarros (y,o)
print (d)

