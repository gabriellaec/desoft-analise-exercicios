a=float(input('Qual o valor do depósito inicial? '))
b=float(input('Qual o valor da taxa de juros? '))
n=1
while n<=24:
    c=a*b**n
    d=c-a
    n+=1
    print(c)
print(d)