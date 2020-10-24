numero_de_cigarros= int(input('Quantos cigarros voce fuma por dia? '))
ha_quantos_anos_fuma= int(input('Ha quantos anos voce fuma? '))
def reducao_de_tempo_de_vida(numero_de_cigarros, ha_quantos_anos_fuma):
    anos_para_dias= ((ha_quantos_anos_fuma)*365)
    tempo_perdido_em_dias= ((numero_de_cigarros * 10) / 1440)
    return(anos_para_dias * tempo_perdido_em_dias)
print (reducao_de_tempo_de_vida(numero_de_cigarros, ha_quantos_anos_fuma))
