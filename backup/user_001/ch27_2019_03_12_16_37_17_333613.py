CIGARROS=float(input("Quantos cigarros vc fuma por dia?"))
ANOS=float(input("Há quantos anos vc fuma?"))
vida=(CIGARROS*ANOS*365)/144
print("Você já perdeu {0:.1f} dias na sua vida".format(vida))