def quantos_cigarros(d, a):
    q= (d*10)/1440
    w= a*365
    y= q*w
    return y

d= int(input('quantos cigarros você fuma por dia? '))
a= int(input('quantos anos você fuma? '))
resultado= quantos_cigarros(d, a)
print(resultado)