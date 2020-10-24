perg = input ("Qual a distância de sua viagem?: ")

if perg<=200:
    custo = perg*0.5
    print("Sua passagem custa: ", custo) 
elif perg>200:
    custo = perg*0.45
    print("Sua passagem custa: ", custo)
    