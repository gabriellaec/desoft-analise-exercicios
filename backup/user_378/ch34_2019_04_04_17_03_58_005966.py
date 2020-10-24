deposito_inicial=float(input('Depósito inicial:'))
taxa_juros=float(input('taxa de juros:'))
i=1
while i<=24:
    total=deposito_inicial*(1+taxa_juros)**i
    i+=1
    print(total)
print(deposito_inicial*(1+taxa_juros)**24-deposito_inicial)