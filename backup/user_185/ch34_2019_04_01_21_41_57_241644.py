deposito_inicial = int(input("Qual é o deposito inicial?" ))
M = deposito_inicial
taxa_juros = int(input("Qual é o juros da poupança? "))
i = 0
while i < tempo:
    M = deposito_inicial*(1+taxa_juros)**i
    print(M)
    i += 1
print(M - deposito_inicial)
    