deposito= float(input("depósito inicial: "))
taxa= float(input("taxa de juros: ")) 
total=0
mes=0
contador=0
while contador<=24:
    mes+=deposito*(1+taxa)
    deposito=mes
    print(mes, '.2f')
    total+=deposito*taxa
    contador+=1

print(total, '.2f')