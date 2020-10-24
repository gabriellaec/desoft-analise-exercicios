a=float(input('qual é o depósito inicial? '))
di = a
b=float(input('qual é o depósito mensal? '))
c=float(input('qual a taxa de juros? '))
n=24
i=1

while i<=n:
    a=a*(1+c) + b
    print('{0:.2f}'.format(a))
    
    i=i+1
x=a-di-24*b
print ('{0:.2f}'.format(x-a))