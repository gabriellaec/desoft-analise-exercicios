dias = int(input("Quantidade de dias: "))        
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

def total_seg(d,h,m,s):
    y = d*24 + h*3600 + m*60 + s
    return y
 
total = total_seg(dias,horas,minutos,segundos)

print("O total em segundos é: {0}".format(total))