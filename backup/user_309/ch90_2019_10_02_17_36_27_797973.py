def segundos_entre(horario1,horario2):
    horario1 = str.split(':')
    horario2 = str.split(':')
    h,m,s = horario1
    h,m,s = horario2
    tempo = int(h)*3600 + int(m)*60 + int(s)
    return tempo(horario2) - tempo(horario1)

    