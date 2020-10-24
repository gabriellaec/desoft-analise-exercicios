def contagem(d, h, m, s):
    soma=(86400*d) + (3600*h) + (60*m) + s
    return soma
dias= int(input('Quantos dias? '))
horas=int(input('quantas horas? '))
minutos=int(input('quantos minutos? '))
segundos=int(input('quantos segundos? '))

la=contagem(dias, horas, minutos, segundos)
print(" a quantidade em segundos eh {0}".format(la))