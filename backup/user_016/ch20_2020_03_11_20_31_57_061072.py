d=input('Qual a distância que você deseja percorrer em km? ')
if d<=200:
    preço=d*0.50
elif d>200:
    preço=d*0.45
print(preço)