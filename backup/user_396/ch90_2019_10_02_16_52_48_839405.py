def segundos_entre(x, y):
    i = 0
    while i < len(x):
        horasX = int(x[0] + x[1])
        horasY =  int(y[0] + y[1])
        minutosX =  int(x[3] + x[4])
        minutosY =  int(y[3] + y[4])
        segundosX = int(x[6] + x[7])
        segundosY = int(y[6] + y[7])
        
        total = ((horasY - horasX) * 3600) + ((minutosY - minutosX) * 60) + (segundosY - segundosX)
        i += 1
    return total