dep_inicial=float(input("Deposito inicial"))
juros=float(input("Taxa de juros: "))

i=1
saldo= dep_inicial

while i<=24:
    saldo= saldo*juros
    print(saldo)
    i+=1

print(saldo-dep_inicial)