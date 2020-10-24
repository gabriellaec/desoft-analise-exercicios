deposito_inicial = float(input('deposito incial :'))
deposito_mensal = float(input('deposito mensal :'))
taxa_de_juros = float(input('taxa de juros :'))

saldo = deposito_inicial 

for m in range(0,24):
    saldo = saldo * (1 + taxa_de_juros) + deposito_mensal
    print('{0:.2f}'.format(saldo))

print('{0:.2f}'.format(saldo - (deposito_inicial + (24 * deposito_mensal))))
