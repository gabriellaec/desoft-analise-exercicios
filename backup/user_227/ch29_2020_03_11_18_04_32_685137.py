deposito_inicial = float(input("Qual o depósito inicial? "))
taxa_de_juros = float(input("Qual a taxa de juros? "))

mês = 0
while mês < 24 :
    cálculo = deposito_inicial*((1+taxa_de_juros)**mês)
    mensal = deposito_inicial*(1+taxa_de_juros)
    print("O valor para o mês {0} é R${1:.2}".format(mês + 1, mensal))
    mês += 1
print("O valor para total é R${0:.2}".format(cálculo))
