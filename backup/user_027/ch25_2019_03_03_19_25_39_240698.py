dist = float(input())
if dist <= 200:
    x = 0.5
elif dist >200:
    x = 0.45
preco = dist*x
print("R$ {0:.2f}".format(preco))
