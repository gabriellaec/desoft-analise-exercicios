km = int(input('Qual distância vai percorrer?: '))
if km <= 200:
    preco = (km*0.5)
else:
    if km > 200:
        preco = (200*0.5) + (km*0.45)
print('{0:.2f}'.format(preco))
