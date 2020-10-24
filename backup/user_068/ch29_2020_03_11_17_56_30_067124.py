a = float(input("Qual o depósito inicial?"))
b= float(input("Qual a taxa de juros de uma poupança"))
x= 0
while x < 24:
    y= a*b*x
    x += 1
    print(y)
print({"0.:2f"}.format (y))
