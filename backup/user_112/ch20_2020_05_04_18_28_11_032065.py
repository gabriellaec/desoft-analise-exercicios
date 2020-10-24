n = input(int('km'))

if n <= 200:
    print(n * 0.50)
if n > 200:
    print((n - 200) * 0.45 + 200 * 0.50)