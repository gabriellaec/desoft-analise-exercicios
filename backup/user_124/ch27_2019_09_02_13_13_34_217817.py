cigarros_dia = int(input("quantos cigarros voce fuma por dia?: "))
tempo_anos = int(input("ha quantos anos voce fuma?: "))


tempo_perdido = (cigarros_dia * 10) / 1440
anos_fumante = tempo_anos / 365
morreu = anos_fumante * tempo_perdido

print(morreu)
    
    
