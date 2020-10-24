dias = int(input('Dias: '))
hrs = int(input('Horas: '))
mins = int(input('Minutos: '))
seg = int(input('Segundos '))
dias = dias*86400
hrs = hrs*3600
mins = mins*60
calculo = dias + hrs + mins + seg
print(calculo)