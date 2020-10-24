dist = float(input())
if dist < 200:
    x = 0.5
    preco = x*dist
elif dist > 200:
    x = 0.45
	preco = preco + (dist-200)*x
print("{:.2f}".format(preco))
