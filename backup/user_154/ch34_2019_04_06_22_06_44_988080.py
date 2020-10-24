depósito_inicial = float(input("Qualç é seu depósito inicial?"))
taxa_de_juros = float(input("Qual é a taxa de juros?"))

i = 1
M = 0

while i <= 24:
    M = depósito_inicial*(1 + taxa_de_juros)**i
    print("Para o {} mês o montante é igual a {}".format(i, M))
    i = i + 1

print("{0:.2f}".format(M - depósito_inicial))