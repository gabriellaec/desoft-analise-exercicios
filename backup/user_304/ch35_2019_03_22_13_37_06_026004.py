a=float(input('qual é o depósito inicial? '))
b=float(input('qual é o depósito mensal? '))
c=float(input('qual a taxa de juros? '))
n=24
i=1

while i<=n:
    if i==1:
        v=a*(1+c)
        print ('{0:.2f}'.format(v))
    elif i>1:
        m=(a+b*i)*(1+c)**i
        print('{0:.2f}'.format(m))
    
    i=i+1
x=(a+b*23)*(1+c)**24
print ('{0:.2f}'.format(x-a))