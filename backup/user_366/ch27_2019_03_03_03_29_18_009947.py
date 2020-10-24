qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'));
qtde_anos = int(input('Há quantos anos você fuma?'));

a = qtde_cigarros
b = qtde_anos

tempo_perdido = (a/144)*365*b
c = tempo_perdido
print('Você já perdeu {0} dias de vida fumando'. format(c));