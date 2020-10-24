depósito_inicial = float(input("Qual é seu depósito inicial?"))
taxa_de_juros = float(input("Qual é a taxa de juros?"))

meses_passados_apos_deposito = 1
valor_do_mês = 0

while i <= 24:
    valor_do_mês = depósito_inicial*(1 + taxa_de_juros)**meses_passados_apos_deposito
    print("Passado {} meses após o depósito incial o montante é igual a {}".format(i, valor_do_mês))
    meses_passados_apos_deposito = meses_passados_apos_deposito + 1

print("{0:.2f}".format(valor_do_mês - depósito_inicial))