km=int(input())
if km <= 200:
    preco_passagem=km*0.5
else:
    preco_passagem=km*0.95
print(round(preco_passagem,2))