def segundos_entre(string1, string2):
    hora1 = int(string1[0:2])
    minuto1 = int(string1[3:5])
    segundo1 = int(string1[6:8])
    
    
    hora2 = int(string2[0:2])
    minuto2 = int(string2[3:5])
    segundo2 = int(string2[6:8])
    
    tempo1 = hora1*3600 + minuto1*60 + segundo1
    tempo2 = hora2*3600 + minuto2*60 + segundo2
    
    diferenca = tempo2 - tempo1
    
    return diferenca
    