def segundos_entre(a,b):
    a = '00:59:59'
    b = '00:10:00'
    segundos_a = a[6:8]
    num_a_s = int(segundos_a)
   
    segundos_b = b[6:8]
    num_b_s = int(segundos_b)
   
    minutos_a = a[3:5] 
    num_a_m = int(minutos_a) * 60
   
    minutos_b = b[3:5]
    num_b_m = int(minutos_b) * 60 
   
    horas_a = a[0:2]
    num_a_h = int(horas_a) * 60 * 60
   
    horas_b = b[0:2]
    num_b_h = int(horas_b) * 60 * 60
    
    horario_a = num_a_s + num_a_m + num_a_h
    horario_b = num_b_s + num_b_m + num_b_h
    final = horario_a - horario_b
    return final