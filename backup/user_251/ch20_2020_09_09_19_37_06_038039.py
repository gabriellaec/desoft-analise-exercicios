def preco_passagem(a):
    y = a
    if a < 200:
        return a*0.5
    else:
        return a*0.45 

a = float(input("quantos quilômetros deseja viajar "))

print(preco_passagem(a))