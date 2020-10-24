recebe_dist = input('Qual a distância que deseja percorrer?');

if recebe_dist < 200:
    preco_viagem = 0.5*recebe_dist;
else:
    preco_viagem = 100 + 0.45*(200-recebe_dist);
    return preco_viagem
round(preco_viagem, 2);