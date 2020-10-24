def contagem(d, h, m, s):
    d=86400*s
    h=3600*s
    m=60*s
    sec=1*s
    return d
    return h
    return m
    return sec
    
dias= int(input('Quantos dias? '))
horas=int(input('quantas horas? '))
minutos=int(input('quantos minutos? '))
segundos=int(input('quantos segundos? '))

la=contagem(dias, horas, minutos, segundos)
print(" a quantidade eh {0}".format(la))
