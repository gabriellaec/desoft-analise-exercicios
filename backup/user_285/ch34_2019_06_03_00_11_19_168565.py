deposito= float(input("depósito inicial: "))
taxa= float(input("taxa de juros: ")) 
soma=0
total=0
for i in range(24):
    total=deposito+deposito*taxa
    print(total, '.2f')
    soma+=total
print(soma, '.2f')