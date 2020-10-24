def calcula_velocidade_media(s,t):
    Velocidade = s/t
    return Velocidade
a = float(input('digite o valor da delta s:'))
b = float(input('digite o valor do tempo gato:'))
c = calcula_velocidade_media(a,b)

print('a velocidade média é: {0}' .format(c))
