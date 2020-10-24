def segundos_entre(primeiro, segundo):
    diferença = 0
    horap = primeiro[:2]
    horas = segundo[:2]
    minp = primeiro[3:5]
    mins = segundo[3:5]
    segp = primeiro[6:8]
    segs = segundo[6:8]
    diferença = ((int(horap)-int(horas))*3600)+((int(minp)-int(mins))*60)+((int(segp)-int(segs)))


    return diferença