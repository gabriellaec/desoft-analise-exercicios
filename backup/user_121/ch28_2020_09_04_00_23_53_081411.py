n = 1
while n < 100:
    x = 1/(2 ** (n - 1))
    y = 1/(2 ** (n))
    n += n
resultado = x + y
print(resultado)