def segundos_entre(horas1, minutos1, segundos1, horas2, minutos2, segundos2):
    seg_min = minutos1 * 60
    seg_hora = horas1 * 3600
    total1 = segundos1 + seg_min + seg_hora
    
    seg_min2 = minutos2 * 60
    seg_hora2 = horas2 * 3600
    total2 = segundos2 + seg_min2 + seg_hora2
    
    subtrac = total2 - total1
    
    return subtrac

