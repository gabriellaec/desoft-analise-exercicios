dias = int(input("escreva uma quantidade de dias"))
horas = int(input("escreva uma quantidade de horas"))
minutos = int(input("escreva uma quantidade de minutos"))
seg = int(input("escreva uma quantidade de seg "))

segundos_totais = (dias*86400) + (horas * 3600) +( minutos*60)+seg

print(segundos_totais)