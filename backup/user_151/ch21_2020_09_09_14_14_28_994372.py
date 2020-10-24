def convert(x, y, z ,w):
    f = (x*24*60*60) + (y*60*60) + (z*60) + w
    return f

d = input('Dias')
h = input('Horas')
m = input('minutos')
s = input('segundos')

c = convert(d, h, m, s)
print(c)