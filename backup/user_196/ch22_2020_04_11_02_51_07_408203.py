a = int(input("Quantos cigarros você fuma por dia: "))
b = int(input("Há quantos anos você fuma?: "))

dias = b*365
dias_perdidos = dias + ((a*10)/(60*24))
print ("Você perdeu dias", dias_perdidos, "de vida")
