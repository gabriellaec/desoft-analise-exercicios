from datetime import datetime

def segundos_entre(hora1,hora2):
    
    FMT = '%H:%M:%S'
    
    saida = datetime.strptime(hora2, FMT) - datetime.strptime(hora1, FMT)
    
    return saida