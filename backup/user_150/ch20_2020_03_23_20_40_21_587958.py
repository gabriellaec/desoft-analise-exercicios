preco = float (input('Qual a distância a ser percorrida? '))
if preco <= 200:
    format((preco*0.50), '.2f')
else:
    format((preco*0.50+(preco-200)*0.45), '.2f')
print ('O preço da passagem é: {0: .2f}' .format(preco))