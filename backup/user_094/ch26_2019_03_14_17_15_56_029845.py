dias = input("Fala ae uma quantidade de dias meu bom: ")
horas = input ("Agora uma quantidade de horas: ")
minu = input ("Duvido vc me falar uns minutos: ")
seg = input ("Ado ado ado quem não me falar uma quantidade de segundos eh viado: ")

def totalseg(dias,horas,minu,seg):
    y=int(dias)*24*60*60 + int(horas)*60*60 + int(minu)*60 *int(seg)
    return y
print ("Carai viado isso dá uns {0} segundos". format (totalseg(dias,horas,minu,seg)))