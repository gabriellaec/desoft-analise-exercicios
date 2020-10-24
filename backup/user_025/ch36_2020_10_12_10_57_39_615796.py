n = int(input('Digite um número: '))

i = 1

while i >= 0:
    n = (n*(n-i))
    i -= n

print(n)