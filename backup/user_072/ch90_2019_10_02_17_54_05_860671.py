def segundos_entre(h1,h2):
    segundos1=int(h1[:2])*3600
    segundos2=int(h1[3:5])*60
    segundos3=int(h1[6:8])
    soma1=(segundos1 + segundos2 + segundos3)
    segundos4=int(h2[:2])*3600
    segundos5=int(h2[3:5])*60
    segundos6=int(h2[6:8])
    soma2= (segundos4 + segundos5 + segundos6)
    return soma2 - soma1
print(segundos_entre('00:59:59','01:00:00'))
    