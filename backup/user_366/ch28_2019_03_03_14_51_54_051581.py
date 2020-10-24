pergunta_velocidade = float(input('Qual era a velocidade do carro?'));
a = pergunta_velocidade

if a > 80:
    b = 5 * (a - 80)
    quit(b) 
else:
    b = 0
    quit(b)

print('A sua multa foi de {0: .2f} reais'. format(b));