a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
juros=(b/100)
i=2
total=0
som=0
while i < 27:
    total=(a*(1+juros)**i)
    i+=1
    som+=total
    print("O valor no mes eh{:.2f}".format(total))
print("o total eh{:.2f}".format(som))

    
    
    