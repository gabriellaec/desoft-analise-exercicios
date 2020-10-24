cigarros_dia = int(input("quantos cigarros voce fuma por dia?: "))
tempo_anos = int(input("ha quantos anos voce fuma?: "))

def cingaro(cigarros_dia, tempo_anos):
    tempo_perdido = (cigarros_dia * 10) / 1440
    anos_fumante = tempo_anos / 365
	ih_carai = anos_fumante * tempo_perdido
    return ih_carai
    
