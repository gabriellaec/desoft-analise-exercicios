quantidade_de_dias = int(input('Qual a quantidade de dias? '))
horas = int(input ('E horas? '))
minutos = int(input ('E minutos? '))
segundos = int (input ('E segundos ? '))

def tempo_em_segundos(quantidade_de_dias, horas, minutos, segundos):
    y = (24*3600*quantidade_de_dias) + (3600*horas) + (60*minutos) + segundos
    return y

print (tempo_em_segundos(quantidade_de_dias,horas,minutos,segundos))


