def segundos_entre(str1,str2):
    segundos1 = int(str1[:2])*3600+int(str1[3:5])*60+int(str1[6:8])
    segundos2 = int(str2[:2])*3600+int(str2[3:5])*60+int(str2[6:8])
    return segundos2-segundos1