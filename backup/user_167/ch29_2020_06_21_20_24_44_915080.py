a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
juros=(b/100)
i=1
total=0
som=0
while i < 25:
    total=(a*(1+juros)**i)
    i+=1
    som+=total
    print(total)
print(som)

    
    