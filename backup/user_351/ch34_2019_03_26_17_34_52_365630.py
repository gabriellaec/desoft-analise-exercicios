deposito_i = float(input("qual o deposito inicial? "))
taxa_juros = float(input("qual a taxa de juros da poupança? "))
meses = 1
ganho = deposito_i*taxa_juros 
while meses <= 24:
    ganho = ganho*taxa_juros
    meses+=1
    print({0:.2f}.format(ganho))
print({0:.2f}.format(ganho))
    