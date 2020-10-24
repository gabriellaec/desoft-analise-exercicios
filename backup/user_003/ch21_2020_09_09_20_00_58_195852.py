dias = int(input("Fala um numero de dias :  "))
hrs = int(input("Fala um numero de horas :  "))
mins= int(input("Fala um numero de minutos :  "))
seg = int(input("Fala um numero de segundos :  "))

dias1 = dias * 86400
hrs1 = hrs * 3600
mins1 = mins * 60

total = mins1 + hrs1 + dias1 + seg

print(total)