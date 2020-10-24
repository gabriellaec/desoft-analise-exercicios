di = float(input("qual o depósito inicial? "))
tj = float(input("qual a taxa de juros? "))
i = 1
s = di + valor
valor = di + di*tj
print (valor)
while i<24:
    s += valor
    valor += valor*tj
    print(valor)
    i+=1
print (s)