d = float(input('deposito inicial'))
a = float(input('taxa de juros'))
t = a/100
m = 1
while(m<25):
    f = d*((1+t)**m)
    m += 1
    print(f)
else:
    print(f-d)