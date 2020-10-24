a = input("Qual a distância que quer viajar")
def preco(a):
    if a<=200:
        return a*0.45
    else:
        return a*0.5