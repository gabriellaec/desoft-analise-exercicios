def segundos(dias, horas, minutos, segundos):
    x = dias*86400 + horas*60**2 + minutos*60 + segundos
    return(x)
segundos(int(input("Escreva uma quantidade de dias ")), 
         int(input("Escreva uma quantidade de horas ")), 
         int(input("Escreva uma quantidade de minutos ")), 
         int(input("Escreva uma quantidade de segundos ")))