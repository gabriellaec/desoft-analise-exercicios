preco= int(input("quntos km?"))
if preco <= 200:
    valor=preco*0.5
else:
    valor= 100 + preco*0.45
print('O valor foi de {:.2f}'.format(valor))