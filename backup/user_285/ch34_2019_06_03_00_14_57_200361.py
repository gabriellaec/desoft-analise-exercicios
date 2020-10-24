deposito= float(input("depósito inicial: "))
taxa= float(input("taxa de juros: ")) 
total=0
mes=0
contador=0
while contador<25:
    mes=deposito*(1+taxa)
    deposito=mes
    total+=mes
    contador+=1
    print(mes, '.2f')
    
print(total, '.2f')