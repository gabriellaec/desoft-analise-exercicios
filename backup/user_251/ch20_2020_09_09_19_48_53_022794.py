def preco_passagem(a):
    y = a
    if a <= 200:
        return a*0.5
    else:
        return (200*0.5) + (a-200)*0.45 

a = float(input("quantos quilômetros deseja viajar "))

print("{0:.2f}".format(preco_passagem(a)))
