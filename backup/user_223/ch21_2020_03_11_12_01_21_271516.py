dias = int(input("Insira o número de dias: "))
horas = int(input("Insira o número de horas: "))
mins = int(input("Insira o número de minutos: "))
seg = int(input("Insira o número de segundos: "))

total = (dias*24*60*60) + horas*60*60 + mins*60 + seg

print("O total é de {} segundos".format(total))