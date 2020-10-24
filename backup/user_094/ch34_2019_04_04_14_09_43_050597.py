di = float(input("qual o depósito inicial? "))
tj = float(input("qual a taxa de juros? "))
i = 1
valor = di + di*tj
s = di + valor
print ("{:.2f}". format(di))
print ("{:.2f}". format(valor))
while i<24:
    s += valor
    valor += valor*tj
    print("{:.2f}". format(valor))
    i+=1
print ("{:.2f}". format(s))