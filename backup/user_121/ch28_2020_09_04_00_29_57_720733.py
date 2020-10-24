n = 1
while n < 100:
    x = 1//(2 ** (n - 1)) + 1//(2 ** n)
    n += 1
    
print(x)