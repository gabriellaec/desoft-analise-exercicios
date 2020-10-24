a=float(input("deposito inicial:")
b=float(input("deposito mensal:")
c=float(input("taxa de juros da poupança:")
mes=1
while mes<24:
        l=a*(1+b)**mes+b
        print(l:.2f)
        mes+=1
n=a*(1+b)**24-a-24*d
print(n:.2f)
        