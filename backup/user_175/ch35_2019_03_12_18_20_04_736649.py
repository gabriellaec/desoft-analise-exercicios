a = float(input())
b = float(input())
c = float(input())
print('{:.2f}'.format(a*(1+c)))
t = 2
d = a*(1+c)
while (t<=24):
    d *= (1+c) 
    print('{:.2f}'.format(d))    
    d += b
    t += 1
print('{:.2f}'.format(d-a-23*b))