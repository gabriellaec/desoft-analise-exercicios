deposito_inicial = int(input("Qual é o deposito inicial?" ))
a = deposito_inicial
taxa_juros = int(input("Qual é o juros da poupança? "))
i = 0
while i < tempo:
    deposito_inicial *= (1+taxa_juros)
    print(deposito_inicial)
    i += 1
print(deposito_inicial - a)
    