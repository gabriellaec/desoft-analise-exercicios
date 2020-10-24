a=input('digite um numero ')
b=input('digite um numero ')

def segundos_entre(string1,string2):
    difer_horas=(int(string2[:2])-int(string1[:2]))*3600
    difer_minutos=(int(string2[3:5])-int(string1[3:5]))*60
    difer_segundos=(int(string2[6:8])-int(string1[6:8]))
    tempo_total=(difer_horas+difer_minutos+difer_segundos)
    print(tempo_total)
    return [string1,string2]
segundos_entre(a,b)
    



    
	