preco = float (input('Qual a distância a ser percorrida? '))
if preco <= 200:
    print(preco*0.50)
else:
    print(preco*0.50+(preco-200)*0.45)