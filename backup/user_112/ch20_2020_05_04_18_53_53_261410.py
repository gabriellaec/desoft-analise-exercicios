n = input('km')
x = float(n)

if x <= 200:
    y = x * 0.50
    print("R$" + "%.2f" % y)
    
if x > 200:
    z = (x - 200) * 0.45 + 200 * 0.50
    print("R$" + "%.2f" % z)