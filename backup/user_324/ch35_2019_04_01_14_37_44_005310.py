deposito=int(input('qual o deposito inicial: '))
taxa=float(input('qual a taxa de juros: '))
deposito_mensal=int(input('deposito mensal: '))
mes=1

while mes<25:
    ganho=deposito*(1+taxa)**mes
    mes+=1
    deposito+=deposito_mensal
    print(round(ganho,2))
print(round(ganho,2))
