cigarros_por_dia= int(input("Quantos cigarros você fuma por dia?:"))
anos= int(input("Há quantos anos você fuma?:"))
cigarros_totais= (cigarros_por_dia*(anos*365))
tempo_perdido_min= (cigarros_totais*10)
tempo_perdido_dias= (tempo_perdido_min/(60*24))

print ("Você perdeu {0:.1f} dias de vida".format(tempo_perdido_dias))