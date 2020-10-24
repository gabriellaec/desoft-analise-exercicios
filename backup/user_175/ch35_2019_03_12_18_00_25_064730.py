a = float(input())
b = float(input())
c = float(input())
v = (a*(1+c))
print(v)
t = 2
while (t<=24):
    v *= (1+c) 
    v += b
    print(v)
    t += 1
print(v-(a+23*b))