x=int(input("digite o valor inicial"))
y=int(input("digite os juros"))
mes=1
valor=x*y
while mes<25:
    valor+=valor*y
    print(valor)
    mes+=1

