d=float(input('Qual a distância que você deseja percorrer em km? '))
if float(d<=200):
    preço=float(d)*0.50
elif float(d>200):
    preço=float(d)*0.45
print('{:.2f}'.format(preço))