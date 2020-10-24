a = float(input("Qual a distância que você deseja percorrer, em km?"))
if a < 200:
          b = 0.50 * a
          return b
else:
          b = 0.45 * a
          return b

print ({0:.2f}".format(b))