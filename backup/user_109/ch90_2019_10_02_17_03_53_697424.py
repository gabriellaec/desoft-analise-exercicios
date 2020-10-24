def segundos_entre (horario1, horario2):
    horas1 = int(horario1[:2])
    horas2 = int(horario2[:2])
    minutos1 = int(horario1[3:5])
    minutos2 = int(horario2[3:5])
    segundos1 = int(horario1[6:])
    segundos2 = int(horario2[6:])

    diferença = (horas2 - horas1)*3600 + (minutos2 - minutos1)*60 + (segundos2 - segundos1)
    return diferença