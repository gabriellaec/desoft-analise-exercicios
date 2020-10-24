depósito_inicial = float(input("Qual é seu depósito inicial?\nDéposito Inicial: "))
deposito_mensal = float(input("Qual vai ser seu déposito mensal?\nDéposito Mensal: "))
taxa_de_juros = float(input("Qual é a taxa de juros?\nTaxa de Juros Mensal: "))

mês = depósito_inicial * (1 + taxa_de_juros)

numero_do_mês = 1

while numero_do_mês <= 24:
    mês = (depósito_inicial + deposito_mensal*numero_do_mês) * (1 + taxa_de_juros) ** (numero_do_mês + 1)
    print("{0:.2f}".format(mês))
    numero_do_mês = numero_do_mês + 1

print("{0:.2f}".format(mês - depósito_inicial - 24*deposito_mensal))