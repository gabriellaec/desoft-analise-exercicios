deposito_inicial=float(input('Qual o empréstimo inicial?'))
deposito_mensal=float(input('Qual o deposito mensal?'))
i=float(input('Qual a taxa de juros'))
total=deposito_inicial+(24*i)
cont=1
while cont<24:
    print(deposito_mensal*i)
    cont+=1
print(total)
