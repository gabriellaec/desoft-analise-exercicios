def vidaFumante(c, a):
    tempo = (a*365*c*10)
    tempo = (tempo/60)/24
    return tempo

c = float(input("Quantos cigarros você fuma por dia? "))
a = float(input("Há quantos anos você fuma? "))

print("Você já perdeu {0:.3f} dias de vida!".format(vidaFumante(c,a)))