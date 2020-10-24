d = input('dia:')
h = input('hora:')
m = input('minuto:')
s = input('segundo:')
d = int(d)
h = int(h)
m = int(m)
s = int(s)
da = a*3600*24
ha = h*3600
ma = m*60
print(da+ha+ma+s)