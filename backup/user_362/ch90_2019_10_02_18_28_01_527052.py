def segundos_entre(horario1,horario2):
    
    termo_1_1=(horario1[:2])
    conver1=int(termo_1_1)
    termo_2_1=(horario1[3:5])
    conver2=int(termo_2_1)
    termo_3_1=(horario1[6:8])
    conver3=int(termo_3_1)
    
    termo_2_1=(horario2[:2])
    conver4=int(termo_2_1)
    termo_2_2=(horario2[3:5])
    conver5=int(termo_2_2)
    termo_3_2=(horario2[6:8])
    conver6=int(termo_3_2)
    
    #somando1:
    horas1=conver1*3600
    minutos1=conver2*60
    segundos1=conver3*1
    soma1=horas1+minutos1+segundos1
    
    #somando2:
    horas2=conver4*3600
    minutos2=conver5*60
    segundos2=conver6*1
    soma2=horas2+minutos2+segundos2
    
    #subtrindo
    total=soma2-soma1
    return total

horario1="14:35:50"
horario2="15:46:00"
print (segundos_entre(horario1,horario2))
