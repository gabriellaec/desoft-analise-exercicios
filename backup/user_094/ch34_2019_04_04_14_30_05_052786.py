di = float(input("qual o depósito inicial? "))
tj = float(input("qual a taxa de juros? "))
i = 1
valor = di + di*tj

print ("{:.2f}". format(valor))
while i<24:
    valor += valor*tj
    print("{:.2f}". format(valor))
    i+=1
print ("{:.2f}". format(valor-di))