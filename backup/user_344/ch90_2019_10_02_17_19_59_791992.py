def segundos_entre(a,b):
    horas = a[0:2] 
    segHa = int(horas) *3600

    minutos = a[3:5]
    segMa = int(minutos) * 60


    segundos = a[6:]
    sega = int(segundos)


    segTa = segHa + segMa + sega
    

    horasb = b[0:2] 
    segHb = int(horasb) *3600

    minutosb = b[3:5]
    segMb = int(minutosb) * 60


    segundosb = b[6:]
    segb = int(segundosb)


    segTb = segHb + segMb + segb



    difseg = segTb - segTa
    return difseg