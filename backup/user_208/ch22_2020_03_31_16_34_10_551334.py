x= int(input("Quantos cigarros você fuma por dia?"))
z= int(input("Há quantos anos você fuma?"))
n = (x*365*z)
y = n*10/1440
print("Você perdeu [0] dias da sua vida.".format(y))
