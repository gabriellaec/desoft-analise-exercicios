def perda(x,y):

    anos_fumando = x*y*365
    total_em_minutos = anos_fumando*10
    tempo_perdido_em_dias = total_em_minutos/1440

    return tempo_perdido_em_dias

a = int(input('Quantos cigarros você fuma por dia? '))
b = int(input('Há quantos você fuma? '))

print (perda(a,b))