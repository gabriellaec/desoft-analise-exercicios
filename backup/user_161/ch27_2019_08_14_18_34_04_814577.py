def vida_perdida(cigarros_por_dia, anos_fumando):
    x = (cigarros_por_dia*10*anos_fumando*365)/(24*60)
    return x

c = int(input("Quantos cigarros você fuma por dia?"))
d = int(input("A quanto tempo você fuma (em anos)?"))

print(vida_perdida(c,d))