a= int(input("Insira os dias:"))
b= int(input("Insira as horas:"))
c= int(input("Insira os minutos:"))
d= int(input("Insira os segundos:"))
total= a*24*60*60+b*60*60+c*60+d
print ("O total de segundos é: {0} segundos".format(total))