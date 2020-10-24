s = float(input("Qual a distância que deseja percorrer? "))
if s <= 200:
    print("{0:.2f}".format(s*0.5))
else:
    print("{0:.2f}".format(100+(s-100)*0.45))