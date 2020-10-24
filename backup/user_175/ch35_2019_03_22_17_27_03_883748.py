a = float(input())
b = float(input())
c = float(input())
t = 0
v = a
meses = 24
while (t<meses):
    v = v + v*c
    print('{:.2f}'.format(v))
    v += b
    t += 1
print('{:.2f}'.format(v-(a+meses*b))