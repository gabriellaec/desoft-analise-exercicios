d = float(input('Qual a distância que você deseja percorrer em km?'))
if d <= 200:
    print(format(d * 0.5, ".2f"))
else:
    print(format(100 + (d - 200) * 0.45, '.2f'))