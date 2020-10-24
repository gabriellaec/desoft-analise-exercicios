cigarros_por_dia = int(input("Quantos cigarros voce fuma por dia?: "))
anos_que_fuma = int(input("Ha quantos anos voce fuma?: "))
qntd_cigarros =  (cigarros_por_dia *365)*anos_que_fuma
tempo_perdido = (qntd_cigarros * 10)/1440
print("Voce perdeu {0} dias de vida por causa do cigarro".format(round(tempo_perdido)))