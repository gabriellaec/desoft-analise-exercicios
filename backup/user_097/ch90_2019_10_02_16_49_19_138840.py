def segundos_entre(horario_1, horario_2):
    h_horario_1 = float(horario_1[:2])
    m_horario_1 = float(horario_1[3:5])
    s_horario_1 = float(horario_1[6:8])

    h_horario_2 = float(horario_2[:2])
    m_horario_2 = float(horario_2[3:5])
    s_horario_2 = float(horario_2[6:8])

    d_horas = h_horario_2 - h_horario_1
    d_minutos = m_horario_2 - m_horario_1
    d_segundos = s_horario_2 - s_horario_1

    total_segundos = (d_horas*60*60) + (d_minutos*60) + (d_segundos)

    return total_segundos