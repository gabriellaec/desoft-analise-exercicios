n = input('km')
x = float(n)

if x <= 200:
    print(x * 0.50)
if x > 200:
    print((x - 200) * 0.45 + 200 * 0.50)