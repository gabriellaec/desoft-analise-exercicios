recebe_dist = float(input('Qual a distância que deseja percorrer?'));

a = recebe_dist

if a <= 200:
    preco_viagem = 0.5*a;
else:
    preco_viagem = 100 + 0.45*(a-200);
    
b = preco_viagem;
round(preco_viagem, 2);
print('O preço da viagem é de {0} reais.'. format(b));