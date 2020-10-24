def segundos_entre(horario1, horario2): #Função para contar os segundos, recebendo dois horarios
    
    #Transformando a string em int para usa-los posteriormente
    horas1 = int(horario1[:2]) 
    minutos1 = int(horario1[3:5])
    segundos1 = int (horario1[6:])
    horas2 = int(horario2[:2])
    minutos2 = int(horario2[3:5])
    segundos2 = int (horario2[6:])
    
    #Converter as horas e os minutos para segundos 
    horas_em_segundos1 = horas1*3600
    minutos_em_segundos1 = minutos1*60
    horas_em_segundos2 = horas2*3600
    minutos_em_segundos2 = minutos2*60
    
    #Somar os segundos com as horas e os minutos em segundos
    segundostotais1 = horas_em_segundos1 + minutos_em_segundos1 + segundos1
    segundostotais2 = horas_em_segundos2 + minutos_em_segundos2 + segundos2
    
    #Diferença de segundos entre os horarios
    diferenca = segundostotais2 - segundostotais1
    if diferenca < 0:
        return -1
    else:
        return diferenca