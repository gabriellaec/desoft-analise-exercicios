a = float(input())
b = float(input())
c = float(input())
d = a
t = 2
print('{:.2f}'.format(a))
while (t<=24):
    d *= (1+c) 
    print('{:.2f}'.format(d))    
    d += b
    t += 1
print('{:.2f}'.format(d-a-23*b))