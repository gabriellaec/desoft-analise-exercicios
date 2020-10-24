x=int(input("digite o valor inicial"))
y=int(input("digite os juros"))
mes=1
valor=x*y
while mes<25:
    valor+=x*y
    print(valor)
    mes+=1
if mes==24:
    print(valor)

