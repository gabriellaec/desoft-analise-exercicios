distancia = float(input("Distancia que quer percorrer: "))
x = 0.50 * distancia
y = (distancia - 200)*0.45 + 100
if distancia <= 200:
     preco = x
else:
    preco = y
    
print("O preço da passagem eh: R${0:.2f}".format(preco))
