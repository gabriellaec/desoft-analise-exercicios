d = float(input('Qual a distância que você deseja percorrer (em Km)?'))
if d <= 200:
    print (d * 0.5)
elif d > 200:
    v = 200*0.5 + (d-200)*0.45
    print ('{:.2f}'.format(v))