a=int(input("A distância que irá percorrer em km"))
if a<200:
    print(0.5*{0:.2f}.format(a))
else:
    print(0.45*{0:.2f}.format(a))