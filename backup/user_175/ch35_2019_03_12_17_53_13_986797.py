a = float(input())
b = float(input())
c = float(input())
d = (a*(1 + c)) 
print('{:.2f}'.format(d))
t = 2
v = d
while (t <= 24):
    v *= (1 + c)
    v += b
    print('{:.2f}' .format(v))
    t += 1
l = (v-(a+23*b))
print('{:.2f}' .format(l))