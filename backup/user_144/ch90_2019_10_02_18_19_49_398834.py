def segundos_entre(string1,string2):
    resultado1 = int(string2[:2]) - int(string1[:2])
    resultado_2 =  int(string2[2:4]) - int(string1[2:4])
    resultado_3 =  int(string2[4:6]) - int(string1[4:6])
    resultado_f = resultado1 + resultado_2 + resultado_3
    return resultado_f
