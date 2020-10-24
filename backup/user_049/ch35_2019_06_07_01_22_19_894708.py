deposito = float(input("deposito: "))
deposito_mensal = float(input("deposito mensal: "))
taxa = float(input("taxa: "))

cont=0
taxa+=1

while cont<24:
    deposito=deposito*taxa
    cont+=1
    print('{:.2f}'.format(deposito))
    
ganho_total=d-dm*24
print('{:.2f}'.format(ganho_total))