d=int(input('qual o depósito inicial? '))
j=float(input('qual é a taxa de juros? '))
n=24
i=1
s=0
while i<=n:
    m=d*(1+j/100)**i
    s=s+d*(1+j/100)**i
    i=i+1
    print('{0:.2f}'.format(m))
    
print('{0:.2f}'.format(s-d))