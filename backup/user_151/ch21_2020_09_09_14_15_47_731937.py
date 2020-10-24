def convert(x, y, z ,w):
    f = (x*24*60*60) + (y*60*60) + (z*60) + w
    return f

d = int(input('Dias'))
h = int(input('Horas'))
m = int(input('minutos'))
s = int(input('segundos'))

c = convert(d, h, m, s)
print(c)