depósito_inicial = float(input("Qualç é seu depósito inicial?"))
taxa_de_juros = float(input("Qual é a taxa de juros?"))
final = inicial

i = 0
mes = 0

while i < 24:
    mes = depósito_inicial*(1 + taxa_de_juros)**i
    print("Para o {} mês o montante é igual a {}".format(i, mes))
    i = i + 1

print("{0:.2f}".format(mes - depósito_inicial))