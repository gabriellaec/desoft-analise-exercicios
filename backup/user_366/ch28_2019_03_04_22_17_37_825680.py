pergunta_velocidade = float(input('Qual era a velocidade do carro, em km/h?'));

a = pergunta_velocidade

if a > 80:
    b = 5 * (a - 80)
    print('A sua multa foi de R${0: .2f}'. format(b)); 
else:
    b = 0
    print('Você não foi multado.');