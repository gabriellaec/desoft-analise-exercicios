d = float(input('deposito inicial'))
a = float(input('taxa de juros'))
t = a/100
m = 1
while(m<25):
    f = d*((1+t)**m)
    m += 1
    print('{0:.2f}'.format(f))
else:
    v = f-d
    print('{0:.2f}'.format(v))