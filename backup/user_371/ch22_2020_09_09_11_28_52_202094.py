def tempo(fumados_dias,anos):
    t = fumados_dias*365*anos
    u = t*(1/144)
    return u

f = input("Quantos cigarros você fuma por dia: ")
a = input("Durante quantos anos: ")

fumados = int(f)
anos = int(a)

dias_perdidos = tempo(fumados, anos)
print("Você perdeu {0} dias de vida".format(dias_perdidos))