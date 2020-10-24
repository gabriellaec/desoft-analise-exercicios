def calcula_velocidade_media(espaço, tempo):
    y= espaço / tempo
    return y

a= (input ('espaço percorrido em km: '))
b= (input ('tempo do percursso em horas: '))
c= int(a)
d= int(b)

e= calcule_velocidade_media(c, d)
print('a velocidade média é {0}'. format(e))