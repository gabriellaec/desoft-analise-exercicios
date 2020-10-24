d=int(input('qual o depósito inicial? '))
j=float(input('qual é a taxa de juros? '))
n=24
i=1
s=0
while i<=24:
    s=s+d*(1+j)**i
    i=i+1
print(s)