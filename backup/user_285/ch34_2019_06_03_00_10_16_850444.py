deposito= float(input("depósito inicial: "))
taxa= float(input("taxa de juros: ")) 
soma=0
for i in range(24):
    total=deposito+=deposito*taxa
    print(total)
    soma+=total
print(soma)