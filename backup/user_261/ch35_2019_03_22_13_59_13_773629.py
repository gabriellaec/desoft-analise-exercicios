a=float(input("deposito inicial:"))
b=float(input("deposito mensal:"))
c=float(input("taxa de juros da poupança:"))
mes=1
while mes<=24:
        l=a*(1+b)**mes+b
        print("{0}:.2f".format(l))
        mes+=1
n=l-a-24*b
print("{0}:.2f".fotmat(n))
        