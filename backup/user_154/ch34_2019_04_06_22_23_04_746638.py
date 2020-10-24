depósito_inicial = float(input("Qual é seu depósito inicial? Depoisito Inicial: "))
taxa_de_juros = float(input("Qual é a taxa de juros? Taxa de Juros Mensais: "))

meses_passados_apos_deposito = 1
valor_do_mês = 0

while meses_passados_apos_deposito <= 24:
    valor_do_mês = depósito_inicial*(1 + taxa_de_juros)**meses_passados_apos_deposito
    print("Passado {0} meses após o depósito incial o montante é igual a {1:.2f}".format(meses_passados_apos_deposito, valor_do_mês))
    meses_passados_apos_deposito = meses_passados_apos_deposito + 1

print("{0:.2f}".format(valor_do_mês - depósito_inicial))