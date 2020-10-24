a = float(input())
b = float(input())
c = float(input())
t = 0
v = a
while t < 24:
    v *= (1+c)
    print('{:.2f}'.format(v))
    v += b
    t += 1
print('{:.2f}'.format(v-(a+23*b))