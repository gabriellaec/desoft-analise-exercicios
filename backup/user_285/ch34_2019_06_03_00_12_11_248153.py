deposito= float(input("depósito inicial: "))
taxa= float(input("taxa de juros: ")) 
soma=0
total=0
contador=0
while contador<25:
    total=deposito+deposito*taxa
    print(total, '.2f')
    soma+=total
    contador+=1
print(soma, '.2f')