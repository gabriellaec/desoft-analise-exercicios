d=int(input('qual o depósito inicial? '))
j=float(input('qual é a taxa de juros? '))
n=24
i=1
s=0
while i<=n:
    n=d*((1+j)**i)
    s=s+d*((1+j)**i)
    i=i+1
print('{0:.2f}'.format(n))
print('{0:.2f}'.format(s))