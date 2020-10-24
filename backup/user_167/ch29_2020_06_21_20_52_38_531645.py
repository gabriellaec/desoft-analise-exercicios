a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
juros=(b/100)
i=0
som=0
while i < 24:
    taxa_mensal=(1+juros)**i
    total= a*taxa_mensal
    som+=total
    i+=1
    print("O valor no mes eh{:.2f}".format(total))
print("o total eh{:.2f}".format(som))

    
    