def segundos_entre(horario1,horario2):
    horario1 = str.split(':')
    horario2 = str.split(':')
    horas1 = horario1[0:3]*3600
    minutos1 = horario1[3:5] * 60
    horas2 = horario2[0:3]
    minutos2 = horario2[3:5]
    x = (horas2 + minutos2) - (horas1 + minutos1)
    return x
   	
    