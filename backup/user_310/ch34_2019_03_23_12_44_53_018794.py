dep_inicial=float(input("Deposito inicial:"))
juros=float(input("Taxa de juros: "))

mes=1
saldo= dep_inicial

while mes<=24:
    saldo+= saldo*juros
    print(saldo)
    mes+=1

print(saldo-dep_inicial)