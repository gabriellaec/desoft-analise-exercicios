qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'));
qtde_anos = int(input('Há quantos anos você fuma?'));

a = qtde_cigarros
b = qtde_anos

tempo_perdido = (1/144)*a*365*b
print('Você já perdeu {0}dias de vida fumando'. format(tempo_perdido));