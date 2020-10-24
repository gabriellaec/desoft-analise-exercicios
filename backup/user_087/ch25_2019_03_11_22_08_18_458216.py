def valor_passagem(x):
    if x == 200:
       return 10
    elif x > 200:
       return (0.5*200 + 0.45*(x- 200))
x = float(input("Que distância você deseja percorrer?")
v = valor_passagem (x)
print ("O valor cobrado será de {o:.2f}".format(v))