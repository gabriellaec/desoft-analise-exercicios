def segundos_entre(horario1, horario2):
  segundos_horario1 = int(horario1[:2])*3600+int(horario1[4:5])*60+int(horario1[7:8])
  segundos_horario2 = int(horario2[:2])*3600+int(horario2[4:5])*60+int(horario2[7:8])
  diferença_segundos = segundos_horario2 - segundos_horario1
  return diferença_segundos