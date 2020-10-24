import math

def segundos_entre(string_1,string_2):
    hora_1 = string_1[0 : 2]
    hora_2 = string_2[0 : 2]
    hora_resultado = int(hora_1) - int(hora_2)
    hora_modulo = math.sqrt(hora_resultado ** 2)
    
    minuto_1 = string_1[3: 5]
    minuto_2 = string_2[3: 5]
    minuto_resultado = int(minuto_1) - int(minuto_2)
    minuto_modulo = math.sqrt(minuto_resultado ** 2)
    
    segundo_1 = string_1[6: 8]
    segundo_2 = string_2[6: 8]
    segundo_resultado = int(segundo_1) - int(segundo_2)
    segundo_modulo = math.sqrt(segundo_resultado ** 2)
    
    converte_segundo_segundo = segundo_modulo * 1
    converte_minuto_segundo = minuto_modulo * 60
    converte_hora_segundo = hora_modulo * 3600
    
    soma_segundo = converte_segundo_segundo + converte_minuto_segundo + converte_hora_segundo
    
    #return hora_modulo, minuto_modulo, segundo_modulo
    return soma_segundo