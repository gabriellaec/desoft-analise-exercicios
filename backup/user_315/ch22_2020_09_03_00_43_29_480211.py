def perda(x,y):

    anos_fumando = x*y*365
    tempo_perdido = anos_fumando*10

    return tempo_perdido

a = int(input('Quantos cigarros você fuma por dia? '))
b = int(input('Há quantos você fuma? '))

print (perda(a,b))