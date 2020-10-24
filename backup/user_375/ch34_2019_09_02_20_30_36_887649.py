d = float(input("Depósito inicial: "))
j = float(input("Taxa de juros: "))

for i in range(1, 25):

    print("Mês ", i, "\n", i * d * (j*0.01 + 1) - d * i)
    i += i
