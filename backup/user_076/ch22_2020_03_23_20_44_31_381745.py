a=int(input("Quantos cigarros você fuma por dia?"))
b=int(input("Há quantos anos você fuma?"))

def tempo_de_vida(cigarrosdiarios, anos):
    n = cigarrosdiarios * anos * 365 # n será o número de cigarros
    y = n * 10  # y será o tempo de vida em minutos
    z = y / (60 * 24)
    return z

print("Você perdeu {} dias de vida".format(tempo_de_vida(a,b)))