pergunta = int(input("Quantos quilometros deseja percorrer?: "))

def cobrado(km):
    if km < 200:
        return km*0.5
    else:
        return km*0.5 + (km - 199)*0.45

print("O preço da viajem foi: {0:.2f}".format(cobrado(pergunta)))
