deposito = float(input("deposito: "))
deposito_mensal = float(input("deposito mensal: "))
taxa = float(input("taxa: "))

cont=0
taxa+=1
valor=deposito

while cont<24:
    deposito=deposito*taxa
    deposito=deposito+deposito_mensal
    cont+=1
    print('{:.2f}'.format(deposito))
    
ganho_total=deposito-valor-deposito_mensal*24
print('{:.2f}'.format(ganho_total))