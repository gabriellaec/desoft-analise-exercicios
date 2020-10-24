dep_inicial=float(input("Deposito inicial: "))
dep_mensal=float(input("Deposito mensal: "))
juros=float(input("Taxa de juros: "))

saldo=dep_inicial
print(saldo)
mes=2

while mes<=24:
    saldo+=(saldo+dep_mensal)*juros
    print(saldo)
    mes+=1

print(saldo-dep_inicial)