distancia_viagem=float(input('Qual a distância que você deseja percorrer na viagem em km? :'))
if distancia_viagem <= 200:
    print('O preço da sua passagem é : {:.2f}'.format(0.5*distancia_viagem))
else:
    print('O preço da sua passagem é : {:.2f}'.format(0.5*200+0.45*(200-distancia_viagem)) 