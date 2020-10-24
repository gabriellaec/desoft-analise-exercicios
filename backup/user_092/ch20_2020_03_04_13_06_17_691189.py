a = int(input("a distância que deseja percorrer: "))
if a<=200:
    b = 0.5*a
else:
    b = 0.5*200 + 0.45*(a-200)
c = float(b)
print("R$ {0:.2f}".format(c))