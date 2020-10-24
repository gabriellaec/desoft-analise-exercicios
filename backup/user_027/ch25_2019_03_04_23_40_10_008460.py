dist = float(input())
x = 0.50
y = 0.45
if dist <= 200:
	preco = x*dist
elif dist > 200:
    preco = (x*200) + ((dist - 200)*y)
print({:.2f}.format(preco))
