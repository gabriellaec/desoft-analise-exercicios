a = float(input())
b = float(input())
c = float(input())
print('{:.2f}'.format(a*(1 + c)))
v = (a*(1 + c))
t = 2
while (t <= 24):
    v *= (1 + c) 
    v += b
    print('{:.2f}' .format(v))
    t += 1
print('{:.2f}' .format(v-(a+23*b)))