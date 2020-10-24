km = int(input('Qual distância vai percorrer?(km): '))
if km < 200 or km == 200:
    preco = (km*0.5)
else:
    if km > 200:
        preco = (200*0.5) + ((km-200)*0.45)
print('O preço da sua viagem será: R${0:.2f}'.format(preco))
