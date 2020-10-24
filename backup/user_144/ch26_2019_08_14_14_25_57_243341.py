dias = int(input("Quantidade de dias: "))        
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de min: "))
seg = int(input("Quantidade de seg: "))

def total_seg(d,h,m,s):
     y = 24*d + 3600*h + 60*m + s
     return y
 
total = total_seg(dias,horas,minutos,seg)

print("O total em segundos é {0}".format(total))