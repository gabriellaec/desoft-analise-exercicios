q = input('quantidade')
t = input('anos')
q = int(q)
t = int(t)
qporano = q*365
qtotal = qporano*t
qemmin = qtotal*10
b = qemmin/60
c = b*3600*24

print(c)