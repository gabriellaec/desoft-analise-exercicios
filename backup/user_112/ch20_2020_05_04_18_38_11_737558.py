n = input('km')
x = float(n)

if x <= 200:
    y = round(x * 0.50, 2)
    print(y)
    
if x > 200:
    z = round((x - 200) * 0.45 + 200 * 0.50, 2)
    print(z)