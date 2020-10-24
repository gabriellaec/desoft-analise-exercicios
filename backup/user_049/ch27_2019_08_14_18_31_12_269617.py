dia = int(input("Quantos cigarros vc fuma por dia? "))
ano = int(input("A quantos anos vc fuma? "))

def vida_perdida(dia,ano):
    vp = (dia*10*ano*365)/(24*60)
    return vp