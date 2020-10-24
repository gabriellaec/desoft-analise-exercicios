a = float(input())
b = float(input())
c = float(input())

v = a

t = 0

meses = 24
while t < meses:
    v = v + v*c
    print('{:.2f}'.format(v))
    v += b
    t += 1
print('{:.2f}'.format(v-(a+meses*b)))