a=int(input("valor deposito inicial?"))
b=int(input("taxa de juros de uma poupanca"))
juros=(b/100)
i=0
total=0
som=0
taxa_mensa=((1+juros)**(1/24)-1)*100
while i < 24:
    total=(a*(1+taxa_mensa)**i)
    i+=1
    print(total)
    som+=total
