def segundos_entre(string1,string2):
    resultado1 = int(string2[:2]) - int(string1[:2])
    resultado_2 =  int(string2[4:5]) - int(string1[4:5])
    resultado_3 =  int(string2[7:8]) - int(string1[7:8])
    resultado_f = resultado1 + resultado_2 + resultado_3
    return resultado_f

