dias = int(input("Fala ae uma quantidade de dias meu bom: "))
horas = int(input("Agora uma quantidade de horas: "))
minu = int(input("Duvido vc me falar uns minutos: "))
seg = int(input("Ado ado ado quem não me falar uma quantidade de segundos eh viado: "))

def totalseg(dias,horas,minu,seg):
    y=dias*24*60*60 + horas*60*60 + minu*60 +seg
    return y
print ("Carai viado isso dá uns {0} segundos". format (totalseg(dias,horas,minu,seg)))