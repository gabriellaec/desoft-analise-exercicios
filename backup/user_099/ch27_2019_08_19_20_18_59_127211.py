def vida_perdida(a,q):
    return (365*a*q*10)/(24*60)
a=float(input("Há quantos anos você fuma?"))
q=int(input("Quantos cigarros você fuma por dia?"))
print("Você perdeu {0} dias de vida!".format(vida_perdida(a,q)))