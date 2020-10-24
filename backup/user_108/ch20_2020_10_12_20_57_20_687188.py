dist = float(input("qual e a distancia"))
preco = 0 
if dist < 200:
   preco = 0.50 * dist
else:
    preco = 0.50 * 200 + (dist - 200) * 0.45
    
 print("{:.2f}".format(preco))
    