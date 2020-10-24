    dias=input("Quantos dias? ")
    horas=input("Quantas horas? ")
    minutos=input("Quantos minutos? ")
    segundos=input("Quantos segundos? ")
    t=dias*24
    u=horas+t*60
    y=u+minutos*60
    total=t+u+y
    print(total)
