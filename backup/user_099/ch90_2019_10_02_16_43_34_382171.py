def segundos_entre(tempo0,tempo1):
    lista_tempo0=tempo0.split(':')
    lista_tempo1=tempo1.split(':')
    tempo_total0=3600*int(lista_tempo0[0])+60*int(lista_tempo0[1])+int(lista_tempo0[2])
    tempo_total1=3600*int(lista_tempo1[0])+60*int(lista_tempo1[1])+int(lista_tempo1[2])
    return 'A difrença é de {0} segundo(s).'.format(tempo_total1-tempo_total0)