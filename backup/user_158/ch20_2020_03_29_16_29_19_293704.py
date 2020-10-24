d=float(input("qual seria a distancia a ser percorida em km ?"))
if d <= 200:
    preco = d*0.5
    print(round(preco,2))
else:
    preco =  d*0.45
    print(round(preco,2))