distancia = int(input('quantos kilometros voce deseja percorrer? '))
if distancia<=200:
    print('R${0:.2f}'.format(distancia*0.5))
elif distancia>200:
    print('R${0:.2f}'.format(distancia*0.45+100))