def segundos(dias, horas, minutos, segundos):
    int(input("insira em sequencia: dias, horas, minutos e segundos: "))
    seg_min = minutos * 60
    seg_hora = horas * 3600
    seg_dias = seg_hora * 24
    total = segundos + seg_min + seg_hora, seg_dias
    return total
    
