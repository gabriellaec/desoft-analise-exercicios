def segundos_entre(string1, string2):
    horas1 = int(string1[0:2])
    minutos1 = int(string1[3:5])
    segundos1 = int(string1[6:])
    horas2 = int(string2[0:2])
    minutos2 = int(string2[3:5])
    segundos2 = int(string2[6:])
    segundos_totais1 = (horas1*3600) + (minutos1*60) + segundos1
    segundos_totais2 = (horas2*3600) + (minutos2*60) + segundos2
    return segundos_totais2 - segundos_totais1