horario1=['00:59:59']
horario2=['01:00:00']
def segundos_entre(horario1,horario2):
    h1=horario1[0,1]
    m1=horario1[3,4]
    s1=horario1[6,7]
    
    h2=horario2[0,1]
    m2=horario2[3,4]
    s2=horario2[6,7]
    
    ht=h1-h2
    mt=