deposito_inicial = float(input("Depósito inicial: "))
deposito_mensal = float(input("Depósito mensal: "))
taxa_de_juros = float(input("Taxa de juros: "))

total = deposito_inicial
juros = taxa_de_juros/100 + 1
mes = 0
while mes < 24:
    total = total*juros + deposito_mensal
    mes += 1
    print("Saldo do mês {0} é de R${1:.2f}".format(mes, total))
        
print ("Total de rendimentos = R${0:.2f}".format(total-deposito_inicial-deposito_mensal*23))