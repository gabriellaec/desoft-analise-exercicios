def segundos_entre(horario1,horario2):
    
    termo_1_1=(horario1[:2])
    termo_2_1=(horario1[3:5])
    termo_3_1=(horario1[6:8])
    
    termo_2_1=(horario2[:2])
    termo_2_2=(horario2[3:5])
    termo_3_2=(horario2[6:8])
    
    #somando1:
    horas1=termo_1_1*3600
    minutos1=termo_2_1*60
    segundos1=termo_3_1*1
    soma1=horas1+minutos1+segundos1
    
    #somando2:
    horas2=termo_2_1*3600
    minutos2=termo_2_2*60
    segundos2=termo_3_2*1
    soma2=horas2+minutos2+segundos2
    
    #subtrindo
    total=soma1-soma2
    return total

horario1="00:59:59"
horario2="01:00:00"
print (segundos_entre(horario1,horario2))