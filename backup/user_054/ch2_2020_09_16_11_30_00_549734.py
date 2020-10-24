1# Está função é para calcular a velocidade média
def velocidade_média (d,t):
    velocidade_média = d / t
    return velocidade_média

print ('qual sua distancia')
d = int (input() )
print ('qual foi o tempo?')
t = int (input() )

print(velocidade_média(d, t))