def segundos_entre(filme1, filme2):
    

    tempo1 = filme1.split(":")
    tempo2 = filme2.split(":")
    tempo1[0] = int(tempo1[0])
    tempo1[1] = int(tempo1[1])
    tempo1[2] = int(tempo1[2])
    tempo2[0] = int(tempo2[0])
    tempo2[1] = int(tempo2[1])
    tempo2[2] = int(tempo2[2])
    horas1 = tempo1[0]*3600
    horas2 = tempo2[0]*3600
    minutos1 = tempo1[1]*60
    minutos2 = tempo2[1]*60
    segundos1 = tempo1[2]
    segundos2 = tempo2[2]
    
    horario2 = horas2 + minutos2 + segundos2
    horario1 = horas1 + minutos1 + segundos1
    
    diferenca = horario2 - horario1
    
    return diferenca
    