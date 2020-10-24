def cigarro_menos_vida(cigarro_por_dia, anos_de_fumo):
    tempo_perdido = ((cigarro_por_dia * (365 * anos_de_fumo))*10)/1440
    return(tempo_perdido)

cigarro_por_dia = int(input("Quantos cigarros voce fuma por dia "))
anos_de_fumo = int(input("Ha quantos anos voce fuma "))

print("voce perdeu {0} dias de vida".format(cigarro_menos_vida(cigarro_por_dia, anos_de_fumo)))