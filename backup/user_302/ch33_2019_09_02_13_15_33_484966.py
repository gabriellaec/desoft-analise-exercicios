a1 = 1
b = 1/2
n = 1
soma = 0
while b < 1/2**99:
    soma = a1 + b
    n = n + 1
    b = b**n
print (soma)