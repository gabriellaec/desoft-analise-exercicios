qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'));
qtde_anos = int(input('Há quantos anos você fuma?'));

tempo_perdido = (1/144)*qtde_cigarros*365*qtde_anos
print('Você já perdeu {0}dias de vida fumando'. format(tempo_perdido));