d = int(input("Digite um numero de dias: "))
h = int(input("Digite um numero de horas: "))
m = int(input("Digite um numero de minutos: "))
s = int(input("Digite um numero de segundos: "))

print("a quantidade de segundos é {}" .format(s*(m*60)*(h*3600)*(d*86400)))