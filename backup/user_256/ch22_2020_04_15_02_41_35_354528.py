a = int(input("Quantos cigarros fuma por dia? "))
b = int(input("Quantos anos vc fuma? "))
cigarrosdia = 10*a
diasemano = 365*b
total=(cigarrosdia*diasemano)/1440
print("Voce perdeu {0} dias de sua vida".format(total))
