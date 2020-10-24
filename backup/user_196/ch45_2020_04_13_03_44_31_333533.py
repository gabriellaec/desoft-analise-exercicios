a = int (input("Qual o número:"))
b = []
while a > 0:
    b.append(a)
    a = int(input("Qual o número:"))
c = b[::-1]
print(c)