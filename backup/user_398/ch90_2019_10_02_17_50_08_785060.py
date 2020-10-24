def segundos_entre(horario1,horario2):
    a=int(horario1[:2])
    b=int(horario2[:2])
    c=int(horario1[3:5])
    d=int(horario2[3:5])
    e=int(horario1[6:])
    f=int(horario2[6:])   
    horas1=a*3600
    horas2=b*3600
    minutos1=c*60
    minutos2=d*60
    segundos1=e
    segundos2=f
    total1=horas1+minutos1+segundos1
    total2=horas2+minutos2+segundos2
    diferenca=total2-total1
    return diferenca