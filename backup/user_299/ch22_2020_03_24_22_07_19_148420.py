q = int(input("Quantos cigarros você fuma por dia?"))
a = float(input("Há quanto anos você fuma?"))
d = a*365
t = q*d/(24*6)
print("Você perdeu {0:.2f} dias".format(t))