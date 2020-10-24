dep_inicial=float(input("Deposito inicial: "))
dep_mensal=float(input("Deposito mensal: "))
juros=float(input("Taxa de juros: "))

saldo=dep_inicial
print(saldo)
i=1

while i<=23:
    ganhos=(saldo*juros)+dep_mensal
    saldo+= ganhos
    print(saldo)
    i+=1

print(saldo-dep_inicial)