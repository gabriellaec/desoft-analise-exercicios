a = float(input())
b = float(input())
c = float(input())
d = a*(1+c)
print('{:.2f}'.format(d))
t = 2
while (t<=24):
    d *= (1+c) 
    d += b
    print('{:.2f}'.format(d))    
    t += 1
print('{:.2f}'.format(d-a-23*b))