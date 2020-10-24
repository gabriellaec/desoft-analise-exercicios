soma1=0
segundos=0
def segundos_entre (hora1, hora2):

#STRING1
    hora1=float(hora1[0:2])     #horas
    minutos1=float(hora1[3:5])    #minutos
    segundos=float(hora1[6:8])   #segundo
    
 #STRING2   
    hora2=float(hora2[0:2])   #horas
    minutos=float(hora2[3:5])   #minutos
    seg=float(hora2[6:8])   #segundos

#Mudanda string 1
    hora1= float(hora1[0:2]*3600)  #hora para segundo
    minutos1=float(hora1[3:5]*60)    #minuto para horas 
    
#Mudanca string 2
    hora2= float(hora2[0:2]*3600)  #hora para segundo
    minutos=float(hora2[3:5]*60)    #minuto para horas 
    
    
    soma1=float(input(hora1 + minutos1+ segundos))
    soma2=float(input(hora2+ minutos +seg))
    
print (soma2 - soma1)
