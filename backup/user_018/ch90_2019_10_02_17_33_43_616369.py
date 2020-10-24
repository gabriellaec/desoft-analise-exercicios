from datetime import datetime

hora_ini = datetime.strptime("14:35:50", '%H:%M:%S')
hora_final = datetime.strptime("15:46:00",'%H:%M:%S')

def segundos_entre(hora_ini,hora_final):
    
    hora_dif = hora_final - hora_ini 
    print("Uptime: %s" % str(hora_dif))
    
    return hora_dif.total_seconds()
