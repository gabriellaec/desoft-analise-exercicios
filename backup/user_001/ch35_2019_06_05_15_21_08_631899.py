deposito_inicial = float(input("Depósito inicial: "))
deposito_mensal = float(input("Depósito mensal: "))
taxa_de_juros = float(input("Taxa de juros: "))

mes = 1
while mes <= 24:
    total = deposito_inicial + mes*deposito_mensal + mes*deposito_mensal*(taxa_de_juros/100)
    mes += 1
    if mes >= 1:
        print("Saldo do mês {0} é de R${1:.2f}".format(mes, total))
        
print ("R${0:.2f}".format(total-deposito_inicial))