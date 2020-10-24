dias = int(input("Fala ae uma quantidade de dias meu bom: "))
horas = int(input("Agora uma quantidade de horas: "))
minu = int(input("Duvido vc me falar uns minutos: "))
seg = int(input("Ado ado ado quem não me falar uma quantidade de segundos eh viado: "))

def totalseg(dias,horas,minu,seg):
    y=int(dias)*24*60*60 + int(horas)*60*60 + int(minu)*60 *int(seg)
    return y
print (totalseg(dias,horas,minu,seg))